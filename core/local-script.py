"""OCR ảnh trang PDF (từ folder _preview_pages) sang text bằng LM Studio (OpenAI-compatible).

Mỗi lần gửi 2 ảnh (trang hiện tại + trang kế) nhưng chỉ trích xuất câu hỏi từ ảnh đầu.
Kèm câu hỏi trước đó (text) làm context cho AI.

Usage:
  python core/local-script.py
  python core/local-script.py -o .md/output.txt
  python core/local-script.py --start-page 8
  python core/local-script.py --images-dir rawtext/_preview_pages --model local-model
  python core/local-script.py --base-url http://localhost:1234/v1
"""

from __future__ import annotations

import argparse
import base64
import re
import sys
import threading
import time
from pathlib import Path
from typing import Any

from openai import OpenAI  # pyright: ignore[reportMissingImports]


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_IMAGES_DIR = PROJECT_ROOT / "rawtext" / "_preview_pages1"
DEFAULT_OUTPUT_TEXT_PATH = PROJECT_ROOT / ".md" / "ck_2022_23.md"
DEFAULT_MODEL = "local-model"
DEFAULT_BASE_URL = "http://localhost:1234/v1"
DEFAULT_API_KEY = "lm-studio"
DEFAULT_PROMPT_PATH = PROJECT_ROOT / "prompt" / "prompt-local.md"

QUESTION_START_RE = re.compile(r"(?m)^Câu\s+\d+\s*:")
OPTION_A_RE = re.compile(r"(?m)^A\.\s*")
ANS_RE = re.compile(r"(?m)^ans:\s*")
MD_FENCE_RE = re.compile(r"```(?:md)?\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)
PAGE_HEADER_RE = re.compile(r"^----- Page (\d+) -----\n", re.MULTILINE)

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


def image_file_to_data_url(image_path: Path) -> str:
	with image_path.open("rb") as handle:
		encoded = base64.b64encode(handle.read()).decode("utf-8")
	suffix = image_path.suffix.lower()
	mime = {
		".png": "image/png",
		".jpg": "image/jpeg",
		".jpeg": "image/jpeg",
		".webp": "image/webp",
	}.get(suffix, "image/png")
	return f"data:{mime};base64,{encoded}"


def resolve_page_image(images_dir: Path, index: int) -> Path | None:
	"""Tìm ảnh trang theo thứ tự 1, 2, 3... (hỗ trợ nhiều định dạng tên)."""
	candidates = [
		images_dir / f"{index}.png",
		images_dir / f"{index}.jpg",
		images_dir / f"{index}.jpeg",
		images_dir / f"{index}.webp",
		images_dir / f"page_{index:04d}.png",
		images_dir / f"page_{index:04d}.jpg",
	]
	for path in candidates:
		if path.exists():
			return path
	return None


def list_page_images(images_dir: Path) -> list[Path]:
	"""Lấy danh sách ảnh trang theo thứ tự từ 1 đến hết."""
	if not images_dir.is_dir():
		raise FileNotFoundError(f"Không tìm thấy folder ảnh: {images_dir}")

	images: list[Path] = []
	index = 1
	while True:
		image_path = resolve_page_image(images_dir, index)
		if image_path is None:
			break
		images.append(image_path)
		index += 1

	if not images:
		raise FileNotFoundError(
			f"Không tìm thấy ảnh nào trong {images_dir}. "
			f"Kỳ vọng tên dạng 1.png, 2.png... hoặc page_0001.png, page_0002.png..."
		)
	return images


def unwrap_md_block(text: str) -> str:
	"""Lấy nội dung trong ```md ... ``` nếu có, không thì trả về text gốc.

	Nếu có nhiều fence (file nhiều trang), ghép tất cả — không chỉ lấy fence đầu.
	"""
	stripped = text.strip()
	fences = list(MD_FENCE_RE.finditer(stripped))
	if not fences:
		return stripped
	if len(fences) == 1:
		return fences[0].group(1).strip()
	return "\n\n".join(match.group(1).strip() for match in fences if match.group(1).strip())


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


def get_last_question_from_output(output_text: str) -> str | None:
	"""Lấy block câu hỏi cuối cùng từ toàn bộ output đã ghi."""
	blocks = split_question_blocks(output_text)
	if not blocks:
		return None
	return blocks[-1]


def extract_question_number(question_block: str) -> int | None:
	match = re.search(r"(?m)^Câu\s+(\d+)\s*:", question_block)
	if not match:
		return None
	return int(match.group(1))


def build_dual_image_section(
	*,
	page_index: int,
	has_context_image: bool,
) -> str:
	"""Hướng dẫn model: 2 ảnh — chỉ trích xuất câu từ ảnh đầu."""
	if has_context_image:
		return (
			"## Hai ảnh đính kèm (theo thứ tự)\n\n"
			f"1. **Ảnh 1 — Trang {page_index} (trang cần trích xuất):** "
			"**Chỉ** xuất câu hỏi nằm trên ảnh này.\n"
			f"2. **Ảnh 2 — Trang {page_index + 1} (chỉ tham khảo):** "
			"Dùng để hiểu ranh giới trang và hoàn thiện câu bị cắt ở **cuối ảnh 1**. "
			"**Không** xuất câu hỏi chỉ xuất hiện trên ảnh 2.\n\n"
			"**Bắt buộc:** Output chỉ chứa câu thuộc ảnh 1. "
			"Ảnh 2 giúp ghép phần còn lại của câu dở ở cuối ảnh 1 — không trích xuất câu mới từ ảnh 2."
		)
	return (
		"## Một ảnh đính kèm\n\n"
		f"Chỉ có **ảnh Trang {page_index}** (trang cuối, không có trang kế). "
		"Trích xuất tất cả câu hỏi trên ảnh này."
	)


def build_page_prompt(
	base_prompt: str,
	last_question: str | None,
	*,
	page_index: int,
	has_context_image: bool,
) -> str:
	"""Ghép context câu trước + hướng dẫn 2 ảnh vào prompt trang hiện tại."""
	image_section = build_dual_image_section(
		page_index=page_index,
		has_context_image=has_context_image,
	)
	parts = [base_prompt, image_section]

	if not last_question:
		return "\n\n".join(parts)

	question_num = extract_question_number(last_question)
	question_label = f"Câu {question_num}" if question_num is not None else "Câu ?"
	next_label = f"Câu {question_num + 1}" if question_num is not None else "câu tiếp theo"
	incomplete = is_incomplete_question(last_question)
	context_image_hint = (
		" Dùng **ảnh 2** (trang kế) nếu phần còn lại của câu nằm ở đầu trang sau."
		if has_context_image
		else ""
	)

	if incomplete:
		status_note = (
			f"{question_label} **chưa hoàn chỉnh** (thiếu nội dung / thiếu A/B/C/D / thiếu hoặc sai đáp án / bị cắt giữa trang). "
			"**Phải sửa câu trước cho đúng** trước khi xuất câu mới. "
			f"Ảnh 1 (và ảnh 2 nếu có) có thể chứa phần còn lại.{context_image_hint}"
		)
		rules = (
			"**Bắt buộc khi câu cuối chưa hoàn chỉnh — SỬA câu trước cho đúng:**\n"
			f"1. SỬA / GHÉP câu text bên dưới với phần còn lại trên **ảnh 1** (và **ảnh 2** nếu cần) "
			f"thành **một {question_label} hoàn chỉnh và đúng** "
			"(đủ nội dung + A/B/C/D... + `ans:` hợp lệ).\n"
			"   - Thiếu / sai đáp án → điền hoặc sửa dòng `ans:` (thêm `[suy luận]` nếu cần).\n"
			"   - Thiếu lựa chọn / nội dung bị cắt → bổ sung từ ảnh 1 hoặc đầu ảnh 2.\n"
			"2. Xuất câu đã sửa/ghép đó **đầu tiên** trong code block ` ```md `.\n"
			f"3. Sau đó mới xuất các câu mới trên **ảnh 1** (từ {next_label} hoặc theo đề gốc).\n"
			"4. **Không** xuất lại các câu đã hoàn chỉnh trước đó (chỉ xuất lại câu cuối đang sửa).\n"
			"5. **Không** giữ marker `[câu bị cắt]` / `[tiếp từ trang trước]` / `[thiếu phần cuối]` trên câu đã sửa xong.\n"
			"6. **Không** xuất câu chỉ có trên ảnh 2."
		)
	else:
		status_note = (
			f"{question_label} **đã hoàn chỉnh** (đủ nội dung + đáp án). "
			f"Tiếp tục trích xuất từ {next_label} trở đi — **chỉ** trên ảnh 1."
		)
		rules = (
			"**Bắt buộc khi câu cuối đã hoàn chỉnh:**\n"
			f"1. **Không** xuất lại {question_label} hoặc bất kỳ câu nào đã có trong output trước.\n"
			f"2. Câu đầu tiên trên **ảnh 1** (nếu là câu mới) phải bắt đầu từ {next_label} hoặc đúng số trên đề gốc.\n"
			"3. Chỉ xuất các câu **mới** xuất hiện trên **ảnh 1**.\n"
			"4. Giữ liên tục số thứ tự — không nhảy số, không lặp số.\n"
			"5. Dùng ảnh 2 chỉ để xác định ranh giới — **không** xuất câu chỉ có trên ảnh 2."
		)

	parts.extend(
		[
			"## Context: câu hỏi cuối cùng trong file output (question.md)\n\n"
			"Pipeline gửi kèm **câu hỏi trước đó** (text) để bạn biết đã làm đến câu nào "
			"và câu đó đã xong hay chưa. Kết hợp với **ảnh 1** (+ ảnh 2 nếu có) để trích xuất đúng.\n\n"
			f"{status_note}\n\n"
			f"{rules}\n\n"
			"### Câu hỏi cuối cùng đã trích xuất\n\n"
			f"```md\n{last_question.strip()}\n```",
		]
	)
	return "\n\n".join(parts)


def wrap_page_block(index: int, text: str, *, is_first: bool, is_last: bool) -> str:
	page_block = f"----- Page {index} -----\n{text}"
	if not is_first:
		page_block = "\n\n" + page_block
	if is_last:
		page_block = page_block.rstrip() + "\n"
	return page_block


def parse_output_pages(content: str) -> list[tuple[int, str]]:
	"""Tách file output thành danh sách (số trang, nội dung trang)."""
	matches = list(PAGE_HEADER_RE.finditer(content))
	if not matches:
		return []

	pages: list[tuple[int, str]] = []
	for index, match in enumerate(matches):
		page_num = int(match.group(1))
		start = match.end()
		end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
		body = content[start:end].strip("\n")
		pages.append((page_num, body))
	return pages


def write_pages_to_file(output_path: Path, pages: list[tuple[int, str]]) -> None:
	"""Ghi lại toàn bộ file từ danh sách trang đã parse."""
	if not pages:
		output_path.write_text("", encoding="utf-8")
		return

	parts: list[str] = []
	total = len(pages)
	for index, (page_num, body) in enumerate(pages):
		parts.append(
			wrap_page_block(
				page_num,
				body,
				is_first=(index == 0),
				is_last=(index == total - 1),
			)
		)
	output_path.write_text("".join(parts), encoding="utf-8")


def read_output_pages(output_path: Path) -> list[tuple[int, str]]:
	if not output_path.exists():
		return []
	return parse_output_pages(output_path.read_text(encoding="utf-8"))


def get_last_processed_page(output_path: Path) -> int:
	pages = read_output_pages(output_path)
	if not pages:
		return 0
	return max(page_num for page_num, _ in pages)


def get_last_question_from_file(output_path: Path) -> str | None:
	"""Lấy câu hỏi cuối cùng từ file output (ưu tiên trang cuối nếu có Page header)."""
	if not output_path.exists():
		return None
	pages = read_output_pages(output_path)
	if pages:
		_, last_body = max(pages, key=lambda item: item[0])
		return get_last_question_from_output(last_body)
	return get_last_question_from_output(output_path.read_text(encoding="utf-8"))


def get_page_body_from_file(output_path: Path, page_index: int) -> str | None:
	for page_num, body in read_output_pages(output_path):
		if page_num == page_index:
			return body
	return None


def truncate_output_from_page(output_path: Path, from_page: int) -> None:
	"""Giữ lại các trang trước from_page, xóa từ from_page trở đi."""
	pages = read_output_pages(output_path)
	kept = [(page_num, body) for page_num, body in pages if page_num < from_page]
	write_pages_to_file(output_path, kept)


def patch_page_in_file(output_path: Path, page_index: int, new_body: str) -> None:
	pages = read_output_pages(output_path)
	updated = False
	for index, (page_num, body) in enumerate(pages):
		if page_num == page_index:
			pages[index] = (page_num, new_body)
			updated = True
			break
	if not updated:
		raise RuntimeError(f"Không tìm thấy Page {page_index} trong {output_path.name} để cập nhật")
	write_pages_to_file(output_path, pages)


def append_page_output(output_path: Path, page_index: int, text: str) -> None:
	"""Ghi thêm một trang mới vào cuối file (không xóa nội dung cũ)."""
	output_path.parent.mkdir(parents=True, exist_ok=True)
	is_first = not output_path.exists() or output_path.stat().st_size == 0
	block = wrap_page_block(page_index, text, is_first=is_first, is_last=True)
	with output_path.open("a", encoding="utf-8") as handle:
		handle.write(block)


def ask_start_page(
	page_total: int,
	output_path: Path,
	cli_start_page: int | None,
) -> int:
	last_done = get_last_processed_page(output_path)
	suggested = last_done + 1 if last_done > 0 else 1
	if suggested > page_total:
		suggested = page_total

	if cli_start_page is not None:
		start_page = cli_start_page
	else:
		print(f"Tổng cộng {page_total} ảnh trang trong folder preview.", flush=True)
		if output_path.exists() and last_done > 0:
			print(
				f"File {output_path.name} đã có đến Page {last_done} "
				f"({output_path.stat().st_size:,} bytes).",
				flush=True,
			)
		else:
			print(f"File {output_path.name} chưa có hoặc đang trống.", flush=True)

		while True:
			raw = input(
				f"Bạn muốn đọc từ trang nào? [1-{page_total}] "
				f"(Enter = {suggested}): "
			).strip()
			if not raw:
				start_page = suggested
				break
			try:
				start_page = int(raw)
			except ValueError:
				print("Vui lòng nhập số nguyên.", flush=True)
				continue
			if 1 <= start_page <= page_total:
				break
			print(f"Chọn số từ 1 đến {page_total}.", flush=True)

	if start_page < 1 or start_page > page_total:
		raise ValueError(f"Trang bắt đầu phải từ 1 đến {page_total}, nhận được: {start_page}")

	if last_done > 0 and start_page <= last_done:
		if cli_start_page is None:
			answer = input(
				f"Page {start_page} đã có trong file. Ghi đè từ Page {start_page} trở đi? [y/N]: "
			).strip().lower()
			if answer not in {"y", "yes"}:
				raise RuntimeError("Đã hủy — chọn trang lớn hơn trang đã xử lý để tiếp tục.")
		truncate_output_from_page(output_path, start_page)
		print(f"Đã xóa Page {start_page} trở đi trong {output_path.name} để ghi lại.", flush=True)

	return start_page


def resolve_last_question_for_page(
	output_path: Path,
	page_index: int,
	start_page: int,
	session_last_page_text: str | None,
) -> str | None:
	if page_index == start_page and start_page > 1:
		return get_last_question_from_file(output_path)
	if session_last_page_text is not None:
		return get_last_question_from_output(session_last_page_text)
	return None


def ensure_server_ready(client: OpenAI, model: str) -> None:
	"""Kiểm tra LM Studio đang chạy và model có sẵn."""
	print(f"Đang kết nối LM Studio và kiểm tra model '{model}'...")
	started = time.monotonic()

	try:
		models = client.models.list()
		available = [item.id for item in models.data]
		if available:
			print(f"  Models có sẵn: {', '.join(available)}")
			if model not in available and model != "local-model":
				print(
					f"  Cảnh báo: '{model}' không nằm trong danh sách. "
					"LM Studio thường dùng tên model đang load — thử --model với id ở trên.",
					file=sys.stderr,
				)
		else:
			print("  Cảnh báo: chưa thấy model nào. Hãy Load model trong LM Studio.", file=sys.stderr)
	except Exception as exc:  # noqa: BLE001
		raise RuntimeError(
			f"Không kết nối được LM Studio tại {client.base_url}. "
			f"Bật Local Server (OpenAI Compatible) rồi thử lại. Chi tiết: {exc}"
		) from exc

	print(f"  Đang warm-up model '{model}'...")
	client.chat.completions.create(
		model=model,
		messages=[{"role": "user", "content": "."}],
		temperature=0,
		max_tokens=1,
	)
	print(f"Đã sẵn sàng model '{model}' ({time.monotonic() - started:.1f}s).")


def ocr_image(
	client: OpenAI,
	image_path: Path,
	model: str,
	prompt: str,
	*,
	page_index: int,
	page_total: int,
	context_image_path: Path | None = None,
	has_last_context: bool = False,
) -> str:
	message_content: list[dict[str, Any]] = [{"type": "text", "text": prompt}]
	message_content.append(
		{"type": "image_url", "image_url": {"url": image_file_to_data_url(image_path)}}
	)
	if context_image_path is not None:
		message_content.append(
			{
				"type": "image_url",
				"image_url": {"url": image_file_to_data_url(context_image_path)},
			}
		)

	prefix = f"[Trang {page_index}/{page_total}]"
	notes: list[str] = []
	if context_image_path is not None:
		notes.append(f"+ ảnh context {context_image_path.name}")
	if has_last_context:
		notes.append("+ câu trước (text)")
	context_note = f" ({', '.join(notes)})" if notes else ""
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
	usage: Any = None

	try:
		stream = client.chat.completions.create(
			model=model,
			messages=[{"role": "user", "content": message_content}],
			temperature=0,
			stream=True,
			stream_options={"include_usage": True},
		)

		for chunk in stream:
			if getattr(chunk, "usage", None) is not None:
				usage = chunk.usage

			choices = getattr(chunk, "choices", None) or []
			if not choices:
				continue

			delta = choices[0].delta
			content = getattr(delta, "content", None) or ""
			if not content:
				continue

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

	stats: list[str] = [f"{elapsed:.1f}s"]
	if usage is not None:
		prompt_tokens = getattr(usage, "prompt_tokens", None)
		completion_tokens = getattr(usage, "completion_tokens", None)
		if isinstance(prompt_tokens, int):
			stats.append(f"prompt={prompt_tokens} token")
		if isinstance(completion_tokens, int):
			stats.append(f"sinh={completion_tokens} token")
			if elapsed > 0:
				stats.append(f"{completion_tokens / elapsed:.1f} tok/s")

	print(f"\r{prefix} Xong OCR ({', '.join(stats)}).{' ' * 20}", flush=True)
	return text


def images_to_text(
	images_dir: Path,
	output_path: Path,
	model: str,
	prompt: str,
	base_url: str,
	api_key: str,
	start_page: int | None = None,
) -> None:
	image_paths = list_page_images(images_dir)
	page_total = len(image_paths)
	start_page = ask_start_page(page_total, output_path, start_page)

	client = OpenAI(base_url=base_url, api_key=api_key)
	ensure_server_ready(client, model)

	output_path.parent.mkdir(parents=True, exist_ok=True)
	print(f"Đã tìm thấy {page_total} ảnh trong {images_dir}", flush=True)
	print(f"Bắt đầu từ Page {start_page}, ghi nối tiếp vào: {output_path}", flush=True)

	session_last_page_text: str | None = None
	processed_count = 0

	for index in range(start_page, page_total + 1):
		image_path = image_paths[index - 1]
		context_image_path = image_paths[index] if index < page_total else None
		if context_image_path is not None:
			print(
				f"[Trang {index}/{page_total}] Đang xử lý {image_path.name} "
				f"(ảnh 1) + {context_image_path.name} (ảnh 2, context)...",
				flush=True,
			)
		else:
			print(
				f"[Trang {index}/{page_total}] Đang xử lý {image_path.name} "
				f"(trang cuối, chỉ 1 ảnh)...",
				flush=True,
			)

		last_question = resolve_last_question_for_page(
			output_path,
			index,
			start_page,
			session_last_page_text,
		)
		was_incomplete = (
			last_question is not None and is_incomplete_question(last_question)
		)
		page_prompt = build_page_prompt(
			prompt,
			last_question,
			page_index=index,
			has_context_image=context_image_path is not None,
		)
		if last_question:
			question_num = extract_question_number(last_question)
			status = "chưa hoàn chỉnh" if was_incomplete else "đã hoàn chỉnh"
			label = f"Câu {question_num}" if question_num is not None else "câu cuối"
			print(
				f"[Trang {index}/{page_total}] Gửi kèm {label} ({status}) "
				f"làm context text ({len(last_question)} ký tự).",
				flush=True,
			)

		text = ocr_image(
			client,
			image_path,
			model,
			page_prompt,
			page_index=index,
			page_total=page_total,
			context_image_path=context_image_path,
			has_last_context=last_question is not None,
		)

		# Câu bị cắt trang trước đã được AI ghép vào trang này → sửa stub ở Page trước
		if was_incomplete and index > 1:
			prev_page_body = get_page_body_from_file(output_path, index - 1)
			if prev_page_body is not None:
				patch_page_in_file(
					output_path,
					index - 1,
					remove_trailing_incomplete(prev_page_body),
				)
				print(
					f"[Trang {index}/{page_total}] Đã gỡ câu chưa hoàn chỉnh khỏi Page {index - 1} "
					"(bản đã sửa/đầy đủ nằm ở trang này).",
					flush=True,
				)

		append_page_output(output_path, index, text)
		session_last_page_text = text
		processed_count += 1

		new_incomplete = get_trailing_incomplete(text)
		if new_incomplete:
			question_num = extract_question_number(new_incomplete)
			label = f"Câu {question_num}" if question_num is not None else "câu cuối"
			print(
				f"[Trang {index}/{page_total}] {label} chưa hoàn chỉnh — "
				"sẽ gửi làm context cho trang sau.",
				flush=True,
			)

		print(f"[Trang {index}/{page_total}] Đã ghi nối tiếp vào {output_path.name}.", flush=True)

	if session_last_page_text is not None:
		final_incomplete = get_trailing_incomplete(session_last_page_text)
		if final_incomplete:
			print(
				"Cảnh báo: trang cuối vẫn còn câu hỏi bị cắt (không còn trang sau để ghép).",
				file=sys.stderr,
			)

	print(
		f"Hoàn tất OCR {processed_count} trang (Page {start_page}→{page_total}) → {output_path}",
		flush=True,
	)


def main() -> int:
	parser = argparse.ArgumentParser(
		description="OCR ảnh trang từ folder _preview_pages sang text bằng LM Studio"
	)
	parser.add_argument(
		"--images-dir",
		default=str(DEFAULT_IMAGES_DIR),
		help="Folder chứa ảnh trang (1.png, 2.png... hoặc page_0001.png...)",
	)
	parser.add_argument(
		"-o",
		"--output",
		default=str(DEFAULT_OUTPUT_TEXT_PATH),
		help="Đường dẫn file văn bản đầu ra",
	)
	parser.add_argument(
		"--model",
		default=DEFAULT_MODEL,
		help="Tên model đang load trong LM Studio (xem Developer → Local Server)",
	)
	parser.add_argument(
		"--base-url",
		default=DEFAULT_BASE_URL,
		help="URL OpenAI-compatible của LM Studio (mặc định http://localhost:1234/v1)",
	)
	parser.add_argument(
		"--api-key",
		default=DEFAULT_API_KEY,
		help="API key (LM Studio chấp nhận bất kỳ chuỗi nào)",
	)
	parser.add_argument(
		"--prompt",
		default=str(DEFAULT_PROMPT_PATH),
		help="Đường dẫn file prompt (.md)",
	)
	parser.add_argument(
		"--start-page",
		type=int,
		default=None,
		help="Trang bắt đầu (bỏ qua hỏi tương tác). Mặc định gợi ý trang kế sau trang đã có trong file.",
	)
	args = parser.parse_args()

	images_dir = Path(args.images_dir).expanduser().resolve()
	output_path = Path(args.output).expanduser().resolve()
	prompt_path = Path(args.prompt).expanduser().resolve()

	try:
		prompt = load_prompt(prompt_path)
		print(f"Đã load prompt từ: {prompt_path}", flush=True)
		images_to_text(
			images_dir,
			output_path,
			args.model,
			prompt,
			args.base_url,
			args.api_key,
			start_page=args.start_page,
		)
		return 0
	except Exception as exc:  # noqa: BLE001
		print(f"Lỗi: {exc}", file=sys.stderr)
		return 1


if __name__ == "__main__":
	raise SystemExit(main())
