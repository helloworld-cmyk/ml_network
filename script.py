"""OCR PDF to text using pdf2image and Ollama.

Usage:
  python script.py input.pdf
  python script.py input.pdf -o output.txt
  python script.py input.pdf --model glm-ocr
"""

from __future__ import annotations

import argparse
import base64
import re
import sys
import tempfile
import threading
import time
from pathlib import Path
from typing import Any

import ollama  # pyright: ignore[reportMissingImports]
from pdf2image import convert_from_path  # pyright: ignore[reportMissingImports]


DEFAULT_INPUT_PDF_PATH = Path(
	"rawtext/ComputerNetwork_Quiz_Bank.pdf"
)
DEFAULT_OUTPUT_TEXT_PATH = Path("question.md")
DEFAULT_MODEL = "minimax-m3:cloud"
DEFAULT_DPI = 220
DEFAULT_POPPLER_PATH = None
DEFAULT_PROMPT_PATH = Path(__file__).resolve().parent / "prompt.md"

QUESTION_START_RE = re.compile(r"(?m)^Câu\s+\d+\s*:")
OPTION_A_RE = re.compile(r"(?m)^A\.\s*")
ANS_RE = re.compile(r"(?m)^ans:\s*")
MD_FENCE_RE = re.compile(r"```(?:md)?\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)

CUT_MARKERS = (
	"câu bị cắt",
	"thiếu phần cuối",
	"tiếp từ trang trước",
	"[câu bị cắt",
)


def load_prompt(prompt_path: Path = DEFAULT_PROMPT_PATH) -> str:
	if not prompt_path.exists():
		raise FileNotFoundError(f"Không tìm thấy file prompt: {prompt_path}")
	return prompt_path.read_text(encoding="utf-8").strip()


def image_file_to_base64(image_path: Path) -> str:
	with image_path.open("rb") as handle:
		return base64.b64encode(handle.read()).decode("utf-8")


def _get(obj: Any, key: str, default: Any = None) -> Any:
	if isinstance(obj, dict):
		return obj.get(key, default)
	return getattr(obj, key, default)


def unwrap_md_block(text: str) -> str:
	"""Lấy nội dung trong ```md ... ``` nếu có, không thì trả về text gốc."""
	stripped = text.strip()
	match = MD_FENCE_RE.search(stripped)
	if match:
		return match.group(1).strip()
	return stripped


def split_question_blocks(text: str) -> list[str]:
	"""Tách OCR output thành các block bắt đầu bằng 'Câu N:'."""
	body = unwrap_md_block(text)
	matches = list(QUESTION_START_RE.finditer(body))
	if not matches:
		return [body] if body.strip() else []

	blocks: list[str] = []
	for index, match in enumerate(matches):
		end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
		block = body[match.start() : end].strip()
		if block:
			blocks.append(block)
	return blocks


def is_incomplete_question(block: str) -> bool:
	"""Câu chưa đủ nếu thiếu A./ans: hoặc có marker bị cắt."""
	lower = block.lower()
	if any(marker in lower for marker in CUT_MARKERS):
		return True
	if OPTION_A_RE.search(block) is None:
		return True
	if ANS_RE.search(block) is None:
		return True
	return False


def get_trailing_incomplete(ocr_text: str) -> str | None:
	"""Trả về câu hỏi cuối trang nếu bị cắt dở, ngược lại None."""
	blocks = split_question_blocks(ocr_text)
	if not blocks:
		return None
	last = blocks[-1]
	if is_incomplete_question(last):
		return last
	return None


def remove_trailing_incomplete(page_text: str) -> str:
	"""Xóa câu hỏi bị cắt ở cuối trang (đã được ghép ở trang sau)."""
	had_fence = "```" in page_text
	blocks = split_question_blocks(page_text)
	if not blocks:
		return page_text
	if not is_incomplete_question(blocks[-1]):
		return page_text

	remaining = blocks[:-1]
	if not remaining:
		body = ""
	else:
		body = "\n\n".join(remaining)

	if had_fence:
		return f"```md\n{body}\n```" if body else "```md\n```"
	return body


def build_page_prompt(base_prompt: str, prev_incomplete: str | None) -> str:
	"""Ghép context câu bị cắt từ trang trước vào prompt trang hiện tại."""
	if not prev_incomplete:
		return base_prompt

	return (
		f"{base_prompt}\n\n"
		"## Context: câu hỏi bị cắt từ trang trước\n\n"
		"Trang trước kết thúc bằng câu hỏi CHƯA ĐỦ bên dưới. "
		"Ảnh hiện tại chứa phần còn lại của câu đó (và có thể thêm câu mới).\n\n"
		"**Bắt buộc:**\n"
		"1. GHÉP phần context với phần còn lại trên ảnh thành **một câu hoàn chỉnh** "
		"(đủ nội dung + A/B/C/D... + `ans:`).\n"
		"2. Xuất câu đã ghép đó **đầu tiên** trong code block ` ```md `.\n"
		"3. Sau đó mới xuất các câu hỏi mới hoàn toàn thuộc trang này.\n"
		"4. **Không** xuất lại các câu đã hoàn chỉnh của trang trước.\n"
		"5. **Không** để lại marker `[câu bị cắt]` trên câu đã ghép xong.\n\n"
		"### Phần câu hỏi bị cắt từ trang trước\n\n"
		f"```md\n{prev_incomplete.strip()}\n```"
	)


def wrap_page_block(index: int, text: str, *, is_first: bool, is_last: bool) -> str:
	page_block = f"----- Page {index} -----\n{text}"
	if not is_first:
		page_block = "\n\n" + page_block
	if is_last:
		page_block = page_block.rstrip() + "\n"
	return page_block


def rewrite_output(output_path: Path, page_outputs: list[str]) -> None:
	"""Ghi lại toàn bộ file từ danh sách output từng trang."""
	parts: list[str] = []
	total = len(page_outputs)
	for index, text in enumerate(page_outputs, start=1):
		parts.append(
			wrap_page_block(
				index,
				text,
				is_first=(index == 1),
				is_last=(index == total),
			)
		)
	output_path.write_text("".join(parts), encoding="utf-8")


def _print_pull_progress(info: Any) -> None:
	status = _get(info, "status") or ""
	completed = _get(info, "completed")
	total = _get(info, "total")
	if isinstance(completed, (int, float)) and isinstance(total, (int, float)) and total > 0:
		pct = completed * 100 / total
		print(f"\r  [{pct:6.2f}%] {status}", end="", flush=True)
	elif status:
		print(f"\r  {status}...", end="", flush=True)


def ensure_model_loaded(client: ollama.Client, model: str) -> None:
	"""Pull (nếu cần) và nạp model vào bộ nhớ, in tiến độ khi có."""
	print(f"Đang load model '{model}'...")

	try:
		for info in client.pull(model, stream=True):
			_print_pull_progress(info)
		print()
	except Exception as exc:  # noqa: BLE001
		print(f"\n  Cảnh báo khi pull model: {exc}", file=sys.stderr)

	print(f"  Đang nạp model '{model}' vào bộ nhớ...")
	started = time.monotonic()
	client.chat(
		model=model,
		messages=[{"role": "user", "content": "."}],
		options={"temperature": 0, "num_predict": 1},
	)
	print(f"Đã load xong model '{model}' ({time.monotonic() - started:.1f}s).")


def ocr_image(
	client: ollama.Client,
	image_path: Path,
	model: str,
	prompt: str,
	*,
	page_index: int,
	page_total: int,
	has_prev_context: bool = False,
) -> str:
	image_data = image_file_to_base64(image_path)
	prefix = f"[Trang {page_index}/{page_total}]"
	context_note = " (+ context câu bị cắt trang trước)" if has_prev_context else ""
	print(f"{prefix} Đang gửi ảnh và xử lý prompt{context_note}...", flush=True)

	stop_heartbeat = threading.Event()
	started = time.monotonic()

	def heartbeat() -> None:
		while not stop_heartbeat.wait(1.0):
			elapsed = time.monotonic() - started
			print(
				f"\r{prefix} Đang xử lý prompt (chưa sinh token)... {elapsed:.0f}s",
				end="",
				flush=True,
			)

	heartbeat_thread = threading.Thread(target=heartbeat, daemon=True)
	heartbeat_thread.start()

	parts: list[str] = []
	token_chunks = 0
	generating = False
	final_chunk: Any = None

	try:
		stream = client.chat(
			model=model,
			messages=[
				{
					"role": "user",
					"content": prompt,
					"images": [image_data],
				}
			],
			options={"temperature": 0},
			stream=True,
		)

		for chunk in stream:
			final_chunk = chunk
			message = _get(chunk, "message")
			content = (_get(message, "content") or "") if message is not None else ""

			if content:
				if not generating:
					stop_heartbeat.set()
					generating = True
					elapsed = time.monotonic() - started
					print(
						f"\r{prefix} Prompt xong sau {elapsed:.1f}s — đang sinh token...",
						flush=True,
					)

				parts.append(content)
				token_chunks += 1
				elapsed = time.monotonic() - started
				chars = sum(len(part) for part in parts)
				print(
					f"\r{prefix} Đang sinh... ~{token_chunks} chunk | {chars} ký tự | {elapsed:.1f}s",
					end="",
					flush=True,
				)
	finally:
		stop_heartbeat.set()
		heartbeat_thread.join(timeout=1.0)

	text = "".join(parts).strip()
	elapsed = time.monotonic() - started

	prompt_tokens = _get(final_chunk, "prompt_eval_count") if final_chunk is not None else None
	eval_tokens = _get(final_chunk, "eval_count") if final_chunk is not None else None
	eval_duration = _get(final_chunk, "eval_duration") if final_chunk is not None else None

	stats: list[str] = [f"{elapsed:.1f}s"]
	if isinstance(prompt_tokens, int):
		stats.append(f"prompt={prompt_tokens} token")
	if isinstance(eval_tokens, int):
		stats.append(f"sinh={eval_tokens} token")
		if isinstance(eval_duration, (int, float)) and eval_duration > 0:
			tps = eval_tokens / (eval_duration / 1e9)
			stats.append(f"{tps:.1f} tok/s")

	print(f"\r{prefix} Xong OCR ({', '.join(stats)}).{' ' * 20}", flush=True)
	return text


def pdf_to_text(
	pdf_path: Path,
	output_path: Path,
	model: str,
	dpi: int,
	poppler_path: str | None,
	prompt: str,
) -> None:
	if not pdf_path.exists():
		raise FileNotFoundError(f"Không tìm thấy file PDF: {pdf_path}")

	client = ollama.Client()
	ensure_model_loaded(client, model)

	output_path.parent.mkdir(parents=True, exist_ok=True)
	output_path.write_text("", encoding="utf-8")
	print(f"Đang ghi lần lượt vào: {output_path}", flush=True)

	with tempfile.TemporaryDirectory(prefix="pdf_ocr_") as temp_dir:
		print(f"Đang chuyển PDF sang ảnh (dpi={dpi})...", flush=True)
		convert_started = time.monotonic()
		images = convert_from_path(
			str(pdf_path),
			dpi=dpi,
			fmt="png",
			output_folder=temp_dir,
			poppler_path=poppler_path,
		)
		print(
			f"Đã chuyển {len(images)} trang sang ảnh "
			f"({time.monotonic() - convert_started:.1f}s).",
			flush=True,
		)

		if not images:
			raise RuntimeError("Không chuyển được trang nào từ PDF sang ảnh")

		page_total = len(images)
		page_outputs: list[str] = []
		prev_incomplete: str | None = None

		for index, image in enumerate(images, start=1):
			image_path = Path(temp_dir) / f"page_{index:04d}.png"
			print(f"[Trang {index}/{page_total}] Đang lưu ảnh...", flush=True)
			image.save(image_path, format="PNG")

			page_prompt = build_page_prompt(prompt, prev_incomplete)
			if prev_incomplete:
				print(
					f"[Trang {index}/{page_total}] Có context câu bị cắt từ trang trước "
					f"({len(prev_incomplete)} ký tự).",
					flush=True,
				)

			text = ocr_image(
				client,
				image_path,
				model,
				page_prompt,
				page_index=index,
				page_total=page_total,
				has_prev_context=bool(prev_incomplete),
			)

			# Câu bị cắt trang trước đã được AI ghép vào trang này → xóa stub cũ
			if prev_incomplete and page_outputs:
				page_outputs[-1] = remove_trailing_incomplete(page_outputs[-1])
				print(
					f"[Trang {index}/{page_total}] Đã gỡ câu bị cắt khỏi trang {index - 1} "
					"(bản đầy đủ nằm ở trang này).",
					flush=True,
				)

			page_outputs.append(text)
			prev_incomplete = get_trailing_incomplete(text)
			if prev_incomplete:
				print(
					f"[Trang {index}/{page_total}] Phát hiện câu bị cắt ở cuối trang — "
					"sẽ gửi làm context cho trang sau.",
					flush=True,
				)

			rewrite_output(output_path, page_outputs)
			print(f"[Trang {index}/{page_total}] Đã ghi vào {output_path.name}.", flush=True)

		if prev_incomplete:
			print(
				"Cảnh báo: trang cuối vẫn còn câu hỏi bị cắt (không còn trang sau để ghép).",
				file=sys.stderr,
			)

	print(f"Hoàn tất OCR {page_total} trang → {output_path}", flush=True)


def main() -> int:
	parser = argparse.ArgumentParser(description="OCR a PDF into plain text using Ollama")
	parser.add_argument("pdf", nargs="?", default=str(DEFAULT_INPUT_PDF_PATH), help="Đường dẫn file PDF đầu vào")
	parser.add_argument(
		"-o",
		"--output",
		default=str(DEFAULT_OUTPUT_TEXT_PATH),
		help="Đường dẫn file văn bản đầu ra",
	)
	parser.add_argument("--model", default=DEFAULT_MODEL, help="Tên model Ollama OCR")
	parser.add_argument("--dpi", type=int, default=DEFAULT_DPI, help="Độ phân giải khi chuyển PDF sang ảnh")
	parser.add_argument(
		"--poppler-path",
		default=DEFAULT_POPPLER_PATH,
		help="Đường dẫn poppler nếu pdf2image không tự tìm thấy",
	)
	parser.add_argument(
		"--prompt",
		default=str(DEFAULT_PROMPT_PATH),
		help="Đường dẫn file prompt (.md)",
	)
	args = parser.parse_args()

	pdf_path = Path(args.pdf).expanduser().resolve()
	output_path = Path(args.output).expanduser().resolve()
	prompt_path = Path(args.prompt).expanduser().resolve()

	try:
		prompt = load_prompt(prompt_path)
		print(f"Đã load prompt từ: {prompt_path}", flush=True)
		pdf_to_text(pdf_path, output_path, args.model, args.dpi, args.poppler_path, prompt)
		return 0
	except Exception as exc:  # noqa: BLE001
		print(f"Lỗi: {exc}", file=sys.stderr)
		return 1


if __name__ == "__main__":
	raise SystemExit(main())
