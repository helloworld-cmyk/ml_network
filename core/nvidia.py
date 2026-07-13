"""OCR ảnh trang PDF (từ folder _preview_pages) sang text bằng NVIDIA API (MiniMax-M3).

Usage:
  python core/nvidia.py
  python core/nvidia.py -o .md/output.txt
  python core/nvidia.py --start-page 8
  python core/nvidia.py --images-dir rawtext/_preview_pages --model minimaxai/minimax-m3

Cần NVIDIA_API_KEY trong .env hoặc biến môi trường.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import threading
import time
from pathlib import Path
from typing import Any

import requests  # pyright: ignore[reportMissingImports]
from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_IMAGES_DIR = PROJECT_ROOT / "rawtext" / "_preview_pages1"
DEFAULT_OUTPUT_TEXT_PATH = PROJECT_ROOT / ".md" / "test.md"
DEFAULT_MODEL = "minimaxai/minimax-m3"
DEFAULT_PROMPT_PATH = PROJECT_ROOT / "prompt" / "prompt.md"
NVIDIA_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
ENV_PATH = PROJECT_ROOT / ".env"

# Lenient: **Câu**, fullwidth colon, lowercase — model đôi khi lệch format prompt.
QUESTION_START_RE = re.compile(
	r"(?m)^(?:\*\*|__)?Câu\s+(\d+)\s*[:：]",
	re.IGNORECASE,
)
OPTION_A_RE = re.compile(r"(?m)^A\.\s*")
OPTION_LETTER_RE = re.compile(r"(?m)^([A-F])\.\s*")
ANS_RE = re.compile(r"(?m)^ans:\s*")
MD_FENCE_RE = re.compile(r"```(?:md)?\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)
PAGE_HEADER_RE = re.compile(r"^----- Page (\d+) -----\n", re.MULTILINE)

CUT_MARKERS = (
	"câu bị cắt",
	"thiếu phần cuối",
	"tiếp từ trang trước",
	"[câu bị cắt",
)


def load_env() -> None:
	load_dotenv(ENV_PATH, override=False)
	if os.environ.get("NVIDIA_API_KEY"):
		return
	if not ENV_PATH.exists():
		return
	for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
		stripped = line.strip()
		if not stripped or stripped.startswith("#"):
			continue
		if "=" not in stripped:
			continue
		key, value = stripped.split("=", 1)
		key = key.strip()
		value = value.strip().strip('"').strip("'")
		if key in {"NVIDIA_API_KEY", "nvidia_api_key", "API_KEY"} and value:
			os.environ.setdefault("NVIDIA_API_KEY", value)
			return


def get_api_key() -> str:
	load_env()
	api_key = os.environ.get("NVIDIA_API_KEY", "").strip()
	if not api_key:
		raise RuntimeError(
			"Thiếu NVIDIA_API_KEY. Thêm vào .env dạng:\n"
			"  NVIDIA_API_KEY=your_key"
		)
	return api_key


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


def _get(obj: Any, key: str, default: Any = None) -> Any:
	if isinstance(obj, dict):
		return obj.get(key, default)
	return getattr(obj, key, default)


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


def _option_letters(block: str) -> list[str]:
	return [match.group(1).upper() for match in OPTION_LETTER_RE.finditer(block)]


def is_incomplete_question(block: str) -> bool:
	"""Câu chưa đủ nếu thiếu A./ans:, có marker bị cắt, hoặc options bị cụt cuối trang."""
	lower = block.lower()
	if any(marker in lower for marker in CUT_MARKERS):
		return True
	if OPTION_A_RE.search(block) is None:
		return True
	if ANS_RE.search(block) is None:
		return True

	# "Chọn N đáp án" nhưng mới có A/B… — thường là câu bị cắt giữa trang.
	choose_n = re.search(r"chọn\s+(\d+)\s+(?:đáp án|phương án)", lower)
	letters = _option_letters(block)
	if choose_n and letters:
		needed = int(choose_n.group(1))
		# Ít nhất cần nhiều hơn N lựa chọn; nếu chỉ còn ≤ N chữ cái đầu → khả năng cao bị cắt.
		if len(letters) <= needed:
			return True

	# Dừng giữa bảng lựa chọn (có A. nhưng chưa tới ans rõ / options không liên tục tới cuối).
	# Ví dụ chỉ A,B rồi hết trang trong khi đề còn C,D...
	if letters and letters[-1] in {"A", "B"} and len(letters) <= 2:
		# Chỉ nghi ngờ khi đề gợi ý nhiều đáp án hoặc chưa có ans hợp lệ.
		ans_match = ANS_RE.search(block)
		ans_tail = block[ans_match.end() :].strip().lower() if ans_match else ""
		if not ans_tail or "không chắc" in ans_tail or "[" in ans_tail:
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


def _rebuild_page_body(blocks: list[str], *, had_fence: bool) -> str:
	body = "\n\n".join(blocks) if blocks else ""
	if had_fence:
		return f"```md\n{body}\n```" if body else "```md\n```"
	return body


def remove_trailing_incomplete(page_text: str) -> str:
	"""Xóa câu hỏi bị cắt ở cuối trang (đã được ghép ở trang sau)."""
	had_fence = "```" in page_text
	blocks = split_question_blocks(page_text)
	if not blocks:
		return page_text
	if not is_incomplete_question(blocks[-1]):
		return page_text
	return _rebuild_page_body(blocks[:-1], had_fence=had_fence)


def remove_last_question(page_text: str) -> str:
	"""Xóa câu cuối trang (đã chuyển sang trang sau — đủ hoặc bản nháp)."""
	had_fence = "```" in page_text
	blocks = split_question_blocks(page_text)
	if not blocks:
		return page_text
	return _rebuild_page_body(blocks[:-1], had_fence=had_fence)


def get_last_question_from_output(output_text: str) -> str | None:
	"""Lấy block câu hỏi cuối cùng từ toàn bộ output đã ghi."""
	blocks = split_question_blocks(output_text)
	if not blocks:
		return None
	return blocks[-1]


def get_first_question_number(ocr_text: str) -> int | None:
	blocks = split_question_blocks(ocr_text)
	if not blocks:
		return None
	return extract_question_number(blocks[0])


def extract_question_number(question_block: str) -> int | None:
	match = QUESTION_START_RE.search(question_block)
	if not match:
		return None
	return int(match.group(1))


def build_page_prompt(
	base_prompt: str,
	last_question: str | None,
) -> str:
	"""Ghép context câu hỏi cuối cùng từ question.md vào prompt trang hiện tại."""
	if not last_question:
		return base_prompt

	question_num = extract_question_number(last_question)
	question_label = f"Câu {question_num}" if question_num is not None else "Câu ?"
	next_label = f"Câu {question_num + 1}" if question_num is not None else "câu tiếp theo"
	incomplete = is_incomplete_question(last_question)

	if incomplete:
		status_note = (
			f"{question_label} **chưa hoàn chỉnh** (thiếu nội dung / thiếu A/B/C/D / thiếu hoặc sai đáp án / bị cắt giữa trang). "
			"**Phải sửa câu trước cho đúng** trước khi xuất câu mới. "
			"Ảnh hiện tại có thể chứa phần còn lại hoặc đủ thông tin để hoàn thiện câu đó."
		)
		rules = (
			"**Bắt buộc khi câu cuối chưa hoàn chỉnh — SỬA câu trước cho đúng:**\n"
			f"1. SỬA / GHÉP context với phần còn lại (hoặc thông tin trên ảnh) thành **một {question_label} hoàn chỉnh và đúng** "
			"(đủ nội dung + A/B/C/D... + `ans:` hợp lệ).\n"
			"   - Thiếu / sai đáp án → điền hoặc sửa dòng `ans:` (thêm `[suy luận]` nếu cần).\n"
			"   - Thiếu lựa chọn / nội dung bị cắt → bổ sung từ ảnh hiện tại.\n"
			"2. Xuất câu đã sửa/ghép đó **đầu tiên** trong code block ` ```md `.\n"
			f"3. Sau đó mới xuất các câu mới hoàn toàn thuộc trang này (từ {next_label} hoặc theo đề gốc).\n"
			"4. **Không** xuất lại các câu đã hoàn chỉnh trước đó (chỉ xuất lại câu cuối đang sửa).\n"
			"5. **Không** giữ marker `[câu bị cắt]` / `[tiếp từ trang trước]` / `[thiếu phần cuối]` trên câu đã sửa xong."
		)
	else:
		status_note = (
			f"{question_label} **đã hoàn chỉnh** (đủ nội dung + đáp án). "
			f"Tiếp tục trích xuất từ {next_label} trở đi theo thứ tự trong ảnh."
		)
		rules = (
			"**Bắt buộc khi câu cuối đã hoàn chỉnh:**\n"
			f"1. **Không** xuất lại {question_label} hoặc bất kỳ câu nào đã có trong output trước.\n"
			f"2. Câu đầu tiên trên ảnh (nếu là câu mới) phải bắt đầu từ {next_label} hoặc đúng số trên đề gốc.\n"
			"3. Chỉ xuất các câu **mới** xuất hiện trên ảnh hiện tại.\n"
			"4. Giữ liên tục số thứ tự — không nhảy số, không lặp số."
		)

	return (
		f"{base_prompt}\n\n"
		"## Context: câu hỏi cuối cùng trong file output (question.md)\n\n"
		"Mỗi lần xử lý ảnh, pipeline **luôn** gửi kèm câu hỏi cuối cùng đã trích xuất để bạn biết "
		"đã làm đến câu nào và câu đó đã xong hay chưa.\n\n"
		f"{status_note}\n\n"
		f"{rules}\n\n"
		"### Câu hỏi cuối cùng đã trích xuất\n\n"
		f"```md\n{last_question.strip()}\n```"
	)


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


def _extract_delta_content(chunk: dict[str, Any]) -> str:
	choices = chunk.get("choices") or []
	if not choices:
		return ""
	delta = choices[0].get("delta") or {}
	content = delta.get("content")
	if isinstance(content, str):
		return content
	if isinstance(content, list):
		parts: list[str] = []
		for item in content:
			if isinstance(item, str):
				parts.append(item)
			elif isinstance(item, dict):
				text = item.get("text")
				if text:
					parts.append(str(text))
		return "".join(parts)
	return ""


def _print_req_banner(prefix: str, label: str) -> None:
	print(f"\n{'=' * 64}", flush=True)
	print(f"  {prefix} {label}", flush=True)
	print(f"{'=' * 64}", flush=True)


def _print_req_input(prefix: str, image_path: Path, prompt: str) -> None:
	"""In input của request hiện tại (prompt text; ảnh chỉ ghi tên, không dump base64)."""
	_print_req_banner(prefix, "INPUT")
	print(f"Ảnh: {image_path.name}", flush=True)
	print(f"Prompt ({len(prompt)} ký tự):", flush=True)
	print("-" * 40, flush=True)
	print(prompt, flush=True)
	print("-" * 40, flush=True)


def _raise_for_nvidia_error(response: requests.Response) -> None:
	if response.ok:
		return
	detail = response.text.strip()
	try:
		payload = response.json()
		if isinstance(payload, dict):
			err = payload.get("error")
			if isinstance(err, dict):
				detail = str(err.get("message") or err)
			elif err:
				detail = str(err)
	except json.JSONDecodeError:
		pass
	raise RuntimeError(f"NVIDIA API lỗi {response.status_code}: {detail}")


def ocr_image(
	api_key: str,
	image_path: Path,
	model: str,
	prompt: str,
	*,
	page_index: int,
	page_total: int,
	has_last_context: bool = False,
) -> str:
	message_content: list[dict[str, Any]] = [
		{"type": "text", "text": prompt},
		{"type": "image_url", "image_url": {"url": image_file_to_data_url(image_path)}},
	]

	prefix = f"[Trang {page_index}/{page_total}]"
	context_note = " (+ context câu cuối từ question.md)" if has_last_context else ""
	_print_req_input(prefix, image_path, prompt)
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
	usage: dict[str, Any] | None = None

	payload = {
		"model": model,
		"messages": [{"role": "user", "content": message_content}],
		"max_tokens": 8192,
		"temperature": 0,
		"top_p": 0.95,
		"stream": True,
	}

	headers = {
		"Authorization": f"Bearer {api_key}",
		"Accept": "text/event-stream",
		"Content-Type": "application/json",
	}

	try:
		response = requests.post(
			NVIDIA_API_URL,
			headers=headers,
			json=payload,
			stream=True,
			timeout=600,
		)
		_raise_for_nvidia_error(response)
		# requests mặc định decode SSE bằng ISO-8859-1 → tiếng Việt thành mojibake (CÃ¢u…).
		response.encoding = "utf-8"

		for raw_line in response.iter_lines(decode_unicode=True):
			if not raw_line:
				continue
			if not raw_line.startswith("data:"):
				continue

			data = raw_line[5:].strip()
			if data == "[DONE]":
				break

			try:
				chunk = json.loads(data)
			except json.JSONDecodeError:
				continue

			if isinstance(chunk.get("usage"), dict):
				usage = chunk["usage"]

			content = _extract_delta_content(chunk)
			if not content:
				continue

			if not generating:
				stop_heartbeat.set()
				generating = True
				elapsed = time.monotonic() - started
				# Xóa dòng heartbeat rồi mở section STREAM OUTPUT của request này.
				print(f"\r{' ' * 80}\r", end="", flush=True)
				print(
					f"{prefix} Prompt xong sau {elapsed:.1f}s — bắt đầu stream:",
					flush=True,
				)
				_print_req_banner(prefix, "STREAM OUTPUT")

			parts.append(content)
			token_chunks += 1
			# In trực tiếp token stream (không \r ghi đè) — request sau sẽ mở banner mới.
			print(content, end="", flush=True)
	finally:
		stop_heartbeat.set()
		heartbeat_thread.join(timeout=1.0)

	text = "".join(parts).strip()
	elapsed = time.monotonic() - started

	stats: list[str] = [f"{elapsed:.1f}s"]
	if usage is not None:
		prompt_tokens = usage.get("prompt_tokens")
		completion_tokens = usage.get("completion_tokens")
		if isinstance(prompt_tokens, int):
			stats.append(f"prompt={prompt_tokens} token")
		if isinstance(completion_tokens, int):
			stats.append(f"sinh={completion_tokens} token")
			if elapsed > 0:
				stats.append(f"{completion_tokens / elapsed:.1f} tok/s")

	if generating:
		print(flush=True)  # kết thúc dòng stream
	_print_req_banner(prefix, f"DONE ({', '.join(stats)}) | {token_chunks} chunk")
	return text


def images_to_text(
	images_dir: Path,
	output_path: Path,
	model: str,
	prompt: str,
	api_key: str,
	start_page: int | None = None,
) -> None:
	image_paths = list_page_images(images_dir)
	page_total = len(image_paths)
	start_page = ask_start_page(page_total, output_path, start_page)

	output_path.parent.mkdir(parents=True, exist_ok=True)
	print(f"Model NVIDIA: {model}", flush=True)
	print(f"Đã tìm thấy {page_total} ảnh trong {images_dir}", flush=True)
	print(f"Bắt đầu từ Page {start_page}, ghi nối tiếp vào: {output_path}", flush=True)

	session_last_page_text: str | None = None
	processed_count = 0

	for index in range(start_page, page_total + 1):
		image_path = image_paths[index - 1]
		print(f"[Trang {index}/{page_total}] Đang xử lý {image_path.name}...", flush=True)

		last_question = resolve_last_question_for_page(
			output_path,
			index,
			start_page,
			session_last_page_text,
		)
		was_incomplete = (
			last_question is not None and is_incomplete_question(last_question)
		)
		page_prompt = build_page_prompt(prompt, last_question)
		if last_question:
			question_num = extract_question_number(last_question)
			status = "chưa hoàn chỉnh" if was_incomplete else "đã hoàn chỉnh"
			label = f"Câu {question_num}" if question_num is not None else "câu cuối"
			print(
				f"[Trang {index}/{page_total}] Gửi kèm {label} ({status}) "
				f"từ question.md ({len(last_question)} ký tự).",
				flush=True,
			)

		text = ocr_image(
			api_key,
			image_path,
			model,
			page_prompt,
			page_index=index,
			page_total=page_total,
			has_last_context=last_question is not None,
		)

		# Câu cuối trang trước (bản nháp/bị cắt) → sau khi trang này có bản đủ:
		# giữ câu đầy đủ ở trang này, gỡ câu cuối khỏi trang trước.
		if index > 1 and last_question is not None:
			prev_num = extract_question_number(last_question)
			new_first_num = get_first_question_number(text)
			same_question_continued = (
				prev_num is not None and prev_num == new_first_num
			)
			if was_incomplete or same_question_continued:
				prev_page_body = get_page_body_from_file(output_path, index - 1)
				if prev_page_body is not None:
					if was_incomplete and not same_question_continued:
						# Chỉ gỡ khi vẫn còn marker/cụt — tránh xóa nhầm câu đã xong.
						patched = remove_trailing_incomplete(prev_page_body)
					else:
						# Trang sau bắt đầu bằng cùng số câu → chuyển hẳn sang trang sau.
						patched = remove_last_question(prev_page_body)
					if patched != prev_page_body:
						patch_page_in_file(output_path, index - 1, patched)
						reason = (
							"cùng số câu xuất hiện đầu trang này"
							if same_question_continued
							else "câu chưa hoàn chỉnh đã được ghép đủ"
						)
						print(
							f"[Trang {index}/{page_total}] Đã gỡ câu cuối khỏi Page {index - 1} "
							f"({reason}).",
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
		description="OCR ảnh trang từ folder _preview_pages sang text bằng NVIDIA API"
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
		help="Model NVIDIA (mặc định: minimaxai/minimax-m3)",
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
		api_key = get_api_key()
		prompt = load_prompt(prompt_path)
		print(f"Đã load prompt từ: {prompt_path}", flush=True)
		images_to_text(
			images_dir,
			output_path,
			args.model,
			prompt,
			api_key,
			start_page=args.start_page,
		)
		return 0
	except Exception as exc:  # noqa: BLE001
		print(f"Lỗi: {exc}", file=sys.stderr)
		return 1


if __name__ == "__main__":
	raise SystemExit(main())
