"""OCR PDF bằng Mistral (Document QnA + OCR images) → text theo format quiz.

Gửi thẳng PDF (từng trang) lên Mistral kèm prompt/prompt-mistral.md.
Ảnh tách từ OCR được lưu vào assets/ cạnh file output.

Usage:
  python core/mistral.py
  python core/mistral.py rawtext/ComputerNetwork_Quiz_Bank.pdf
  python core/mistral.py -o .md/output.md --start-page 2
  python core/mistral.py --model mistral-small-latest
"""

from __future__ import annotations

import argparse
import base64
import os
import re
import sys
import threading
import time
from io import BytesIO
from pathlib import Path
from typing import Any

from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]
from mistralai.client import Mistral  # pyright: ignore[reportMissingImports]
from pypdf import PdfReader, PdfWriter  # pyright: ignore[reportMissingImports]


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PDF_PATH = PROJECT_ROOT / "rawtext" / "ComputerNetwork_Quiz_Bank.pdf"
DEFAULT_OUTPUT_TEXT_PATH = PROJECT_ROOT / ".md" / "ck_2022_23.md"
DEFAULT_PROMPT_PATH = PROJECT_ROOT / "prompt" / "prompt-mistral.md"
DEFAULT_CHAT_MODEL = "mistral-small-latest"
DEFAULT_OCR_MODEL = "mistral-ocr-latest"
ENV_PATH = PROJECT_ROOT / ".env"

QUESTION_START_RE = re.compile(r"(?m)^Câu\s+\d+\s*:")
OPTION_A_RE = re.compile(r"(?m)^A\.\s*")
ANS_RE = re.compile(r"(?m)^ans:\s*")
MD_FENCE_RE = re.compile(r"```(?:md)?\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)
PAGE_HEADER_RE = re.compile(r"^----- Page (\d+) -----\n", re.MULTILINE)
IMG_MARKDOWN_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

CUT_MARKERS = (
	"câu bị cắt",
	"thiếu phần cuối",
	"tiếp từ trang trước",
	"[câu bị cắt",
)


def load_env() -> None:
	load_dotenv(ENV_PATH, override=False)
	# Hỗ trợ .env dạng "api_key = ..." (không chuẩn dotenv KEY=VALUE)
	if os.environ.get("MISTRAL_API_KEY"):
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
		if key in {"MISTRAL_API_KEY", "api_key", "API_KEY"} and value:
			os.environ.setdefault("MISTRAL_API_KEY", value)
			return


def get_api_key() -> str:
	load_env()
	api_key = os.environ.get("MISTRAL_API_KEY", "").strip()
	if not api_key:
		raise RuntimeError(
			"Thiếu MISTRAL_API_KEY. Thêm vào .env dạng:\n"
			"  MISTRAL_API_KEY=your_key\n"
			"hoặc: api_key = your_key"
		)
	return api_key


def load_prompt(prompt_path: Path = DEFAULT_PROMPT_PATH) -> str:
	if not prompt_path.exists():
		raise FileNotFoundError(f"Không tìm thấy file prompt: {prompt_path}")
	return prompt_path.read_text(encoding="utf-8").strip()


def _get(obj: Any, key: str, default: Any = None) -> Any:
	if isinstance(obj, dict):
		return obj.get(key, default)
	return getattr(obj, key, default)


def unwrap_md_block(text: str) -> str:
	"""Lấy nội dung trong ```md ... ``` nếu có, không thì trả về text gốc."""
	stripped = text.strip()
	fences = list(MD_FENCE_RE.finditer(stripped))
	if not fences:
		return stripped
	if len(fences) == 1:
		return fences[0].group(1).strip()
	return "\n\n".join(match.group(1).strip() for match in fences if match.group(1).strip())


def split_question_blocks(text: str) -> list[str]:
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
	lower = block.lower()
	if any(marker in lower for marker in CUT_MARKERS):
		return True
	if OPTION_A_RE.search(block) is None:
		return True
	if ANS_RE.search(block) is None:
		return True
	return False


def get_trailing_incomplete(ocr_text: str) -> str | None:
	blocks = split_question_blocks(ocr_text)
	if not blocks:
		return None
	last = blocks[-1]
	if is_incomplete_question(last):
		return last
	return None


def remove_trailing_incomplete(page_text: str) -> str:
	had_fence = "```" in page_text
	blocks = split_question_blocks(page_text)
	if not blocks:
		return page_text
	if not is_incomplete_question(blocks[-1]):
		return page_text

	remaining = blocks[:-1]
	body = "\n\n".join(remaining) if remaining else ""
	if had_fence:
		return f"```md\n{body}\n```" if body else "```md\n```"
	return body


def get_last_question_from_output(output_text: str) -> str | None:
	blocks = split_question_blocks(output_text)
	if not blocks:
		return None
	return blocks[-1]


def extract_question_number(question_block: str) -> int | None:
	match = re.search(r"(?m)^Câu\s+(\d+)\s*:", question_block)
	if not match:
		return None
	return int(match.group(1))


def build_page_prompt(
	base_prompt: str,
	last_question: str | None,
	*,
	page_index: int,
	page_total: int,
	saved_images: list[str] | None = None,
) -> str:
	parts = [
		base_prompt,
		"",
		f"## Trang đang xử lý: Page {page_index}/{page_total}",
		"",
		"Chỉ trích xuất câu hỏi thuộc **trang PDF này**. Không thêm `----- Page N -----` (script tự thêm).",
	]
	if saved_images:
		parts.extend(
			[
				"",
				"## Ảnh đã lưu từ trang này (dùng cho dòng `img:`)",
				"",
				*[f"- `{name}`" for name in saved_images],
				"",
				"Nếu câu hỏi tham chiếu hình, ghi `img: assets/<tên-file>` với tên trong danh sách trên.",
			]
		)

	if not last_question:
		return "\n".join(parts)

	question_num = extract_question_number(last_question)
	question_label = f"Câu {question_num}" if question_num is not None else "Câu ?"
	next_label = f"Câu {question_num + 1}" if question_num is not None else "câu tiếp theo"
	incomplete = is_incomplete_question(last_question)

	if incomplete:
		status_note = (
			f"{question_label} **chưa hoàn chỉnh** (thiếu nội dung / thiếu A/B/C/D / thiếu hoặc sai đáp án / bị cắt giữa trang). "
			"**Phải sửa câu trước cho đúng** trước khi xuất câu mới. "
			"Trang hiện tại có thể chứa phần còn lại hoặc đủ thông tin để hoàn thiện câu đó."
		)
		rules = (
			"**Bắt buộc khi câu cuối chưa hoàn chỉnh — SỬA câu trước cho đúng:**\n"
			f"1. SỬA / GHÉP context với phần còn lại (hoặc thông tin trên trang) thành **một {question_label} hoàn chỉnh và đúng** "
			"(đủ nội dung + A/B/C/D... + `ans:` hợp lệ).\n"
			"   - Thiếu / sai đáp án → điền hoặc sửa dòng `ans:` (thêm `[suy luận]` nếu cần).\n"
			"   - Thiếu lựa chọn / nội dung bị cắt → bổ sung từ trang hiện tại.\n"
			"2. Xuất câu đã sửa/ghép đó **đầu tiên** trong code block ` ```md `.\n"
			f"3. Sau đó mới xuất các câu mới hoàn toàn thuộc trang này (từ {next_label} hoặc theo đề gốc).\n"
			"4. **Không** xuất lại các câu đã hoàn chỉnh trước đó (chỉ xuất lại câu cuối đang sửa).\n"
			"5. **Không** giữ marker `[câu bị cắt]` / `[tiếp từ trang trước]` / `[thiếu phần cuối]` trên câu đã sửa xong."
		)
	else:
		status_note = (
			f"{question_label} **đã hoàn chỉnh** (đủ nội dung + đáp án). "
			f"Tiếp tục trích xuất từ {next_label} trở đi theo thứ tự trong trang."
		)
		rules = (
			"**Bắt buộc khi câu cuối đã hoàn chỉnh:**\n"
			f"1. **Không** xuất lại {question_label} hoặc bất kỳ câu nào đã có trong output trước.\n"
			f"2. Câu đầu tiên trên trang (nếu là câu mới) phải bắt đầu từ {next_label} hoặc đúng số trên đề gốc.\n"
			"3. Chỉ xuất các câu **mới** xuất hiện trên trang hiện tại.\n"
			"4. Giữ liên tục số thứ tự — không nhảy số, không lặp số."
		)

	parts.extend(
		[
			"",
			"## Context: câu hỏi cuối cùng trong file output (question.md)",
			"",
			"Mỗi lần xử lý trang, pipeline **luôn** gửi kèm câu hỏi cuối cùng đã trích xuất để bạn biết "
			"đã làm đến câu nào và câu đó đã xong hay chưa.",
			"",
			status_note,
			"",
			rules,
			"",
			"### Câu hỏi cuối cùng đã trích xuất",
			"",
			f"```md\n{last_question.strip()}\n```",
		]
	)
	return "\n".join(parts)


def wrap_page_block(index: int, text: str, *, is_first: bool, is_last: bool) -> str:
	page_block = f"----- Page {index} -----\n{text}"
	if not is_first:
		page_block = "\n\n" + page_block
	if is_last:
		page_block = page_block.rstrip() + "\n"
	return page_block


def parse_output_pages(content: str) -> list[tuple[int, str]]:
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
		print(f"Tổng cộng {page_total} trang PDF.", flush=True)
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


def count_pdf_pages(pdf_path: Path) -> int:
	reader = PdfReader(str(pdf_path))
	return len(reader.pages)


def extract_page_pdf_bytes(pdf_path: Path, page_index_0: int) -> bytes:
	reader = PdfReader(str(pdf_path))
	if page_index_0 < 0 or page_index_0 >= len(reader.pages):
		raise IndexError(f"Trang PDF không hợp lệ: {page_index_0 + 1}")
	writer = PdfWriter()
	writer.add_page(reader.pages[page_index_0])
	buffer = BytesIO()
	writer.write(buffer)
	return buffer.getvalue()


def encode_pdf_data_url(pdf_bytes: bytes) -> str:
	encoded = base64.b64encode(pdf_bytes).decode("utf-8")
	return f"data:application/pdf;base64,{encoded}"


def decode_image_base64(image_base64: str) -> bytes:
	raw = image_base64.strip()
	if raw.startswith("data:") and "," in raw:
		raw = raw.split(",", 1)[1]
	return base64.b64decode(raw)


def assets_dir_for_output(output_path: Path) -> Path:
	return output_path.parent / "assets"


def save_ocr_images(
	page_images: list[Any],
	assets_dir: Path,
	*,
	page_index: int,
) -> list[str]:
	"""Lưu ảnh OCR vào assets/, trả về danh sách tên file đã lưu."""
	if not page_images:
		return []

	assets_dir.mkdir(parents=True, exist_ok=True)
	saved: list[str] = []
	for img_index, img in enumerate(page_images):
		img_id = str(_get(img, "id") or f"img-{img_index}.jpeg")
		image_b64 = _get(img, "image_base64")
		if not image_b64:
			continue

		# page_0001_img-0.jpeg — tránh trùng giữa các trang
		stem = Path(img_id).stem
		suffix = Path(img_id).suffix or ".jpeg"
		filename = f"page_{page_index:04d}_{stem}{suffix}"
		out_path = assets_dir / filename
		out_path.write_bytes(decode_image_base64(str(image_b64)))
		saved.append(filename)
	return saved


def rewrite_img_refs(text: str, saved_images: list[str], page_index: int) -> str:
	"""Đổi ![img-0.jpeg](img-0.jpeg) / img: img-0.jpeg → assets/page_XXXX_img-0.jpeg."""
	if not saved_images:
		return text

	id_to_asset: dict[str, str] = {}
	for filename in saved_images:
		# page_0001_img-0.jpeg → img-0.jpeg
		prefix = f"page_{page_index:04d}_"
		original = filename[len(prefix) :] if filename.startswith(prefix) else filename
		id_to_asset[original] = f"assets/{filename}"
		id_to_asset[filename] = f"assets/{filename}"

	def replace_md(match: re.Match[str]) -> str:
		alt, target = match.group(1), match.group(2)
		base = Path(target).name
		mapped = id_to_asset.get(base) or id_to_asset.get(target)
		if mapped:
			return f"img: {mapped}"
		return match.group(0)

	text = IMG_MARKDOWN_RE.sub(replace_md, text)

	def replace_img_line(match: re.Match[str]) -> str:
		target = match.group(1).strip()
		base = Path(target).name
		mapped = id_to_asset.get(base) or id_to_asset.get(target)
		if mapped:
			return f"img: {mapped}"
		return match.group(0)

	text = re.sub(r"(?m)^img:\s*(.+)$", replace_img_line, text)
	return text


def ocr_pdf_page(
	client: Mistral,
	pdf_bytes: bytes,
	*,
	ocr_model: str,
	page_index: int,
	page_total: int,
) -> Any:
	prefix = f"[Trang {page_index}/{page_total}]"
	print(f"{prefix} Đang OCR PDF (mistral-ocr)...", flush=True)
	started = time.monotonic()
	response = client.ocr.process(
		model=ocr_model,
		document={
			"type": "document_url",
			"document_url": encode_pdf_data_url(pdf_bytes),
		},
		include_image_base64=True,
		include_blocks=True,
	)
	elapsed = time.monotonic() - started
	pages = _get(response, "pages") or []
	n_images = 0
	if pages:
		n_images = len(_get(pages[0], "images") or [])
	print(
		f"{prefix} OCR xong ({elapsed:.1f}s, {n_images} ảnh).",
		flush=True,
	)
	return response


def extract_page_with_chat(
	client: Mistral,
	pdf_bytes: bytes,
	prompt: str,
	*,
	chat_model: str,
	page_index: int,
	page_total: int,
	has_last_context: bool = False,
) -> str:
	prefix = f"[Trang {page_index}/{page_total}]"
	context_note = " (+ context câu cuối)" if has_last_context else ""
	print(f"{prefix} Đang gửi PDF + prompt lên chat{context_note}...", flush=True)

	stop_heartbeat = threading.Event()
	started = time.monotonic()

	def heartbeat() -> None:
		while not stop_heartbeat.wait(1.0):
			elapsed = time.monotonic() - started
			print(
				f"\r{prefix} Đang chờ Mistral... {elapsed:.0f}s",
				end="",
				flush=True,
			)

	heartbeat_thread = threading.Thread(target=heartbeat, daemon=True)
	heartbeat_thread.start()

	try:
		response = client.chat.complete(
			model=chat_model,
			temperature=0,
			messages=[
				{
					"role": "user",
					"content": [
						{"type": "text", "text": prompt},
						{
							"type": "document_url",
							"document_url": encode_pdf_data_url(pdf_bytes),
						},
					],
				}
			],
		)
	finally:
		stop_heartbeat.set()
		heartbeat_thread.join(timeout=1.0)

	elapsed = time.monotonic() - started
	choice = (_get(response, "choices") or [None])[0]
	message = _get(choice, "message") if choice is not None else None
	content = _get(message, "content") if message is not None else None
	if isinstance(content, list):
		parts: list[str] = []
		for item in content:
			if isinstance(item, str):
				parts.append(item)
			else:
				text = _get(item, "text")
				if text:
					parts.append(str(text))
		text = "".join(parts).strip()
	else:
		text = (content or "").strip() if isinstance(content, str) else str(content or "").strip()

	usage = _get(response, "usage")
	stats = [f"{elapsed:.1f}s"]
	if usage is not None:
		prompt_tokens = _get(usage, "prompt_tokens")
		completion_tokens = _get(usage, "completion_tokens")
		if isinstance(prompt_tokens, int):
			stats.append(f"prompt={prompt_tokens}")
		if isinstance(completion_tokens, int):
			stats.append(f"out={completion_tokens}")

	print(f"\r{prefix} Chat xong ({', '.join(stats)}).{' ' * 20}", flush=True)
	return text


def pdf_to_text(
	pdf_path: Path,
	output_path: Path,
	prompt: str,
	*,
	chat_model: str,
	ocr_model: str,
	start_page: int | None = None,
	skip_ocr_images: bool = False,
) -> None:
	if not pdf_path.exists():
		raise FileNotFoundError(f"Không tìm thấy PDF: {pdf_path}")

	page_total = count_pdf_pages(pdf_path)
	if page_total < 1:
		raise RuntimeError(f"PDF không có trang nào: {pdf_path}")

	start_page = ask_start_page(page_total, output_path, start_page)
	client = Mistral(api_key=get_api_key())
	assets_dir = assets_dir_for_output(output_path)

	output_path.parent.mkdir(parents=True, exist_ok=True)
	print(f"PDF: {pdf_path} ({page_total} trang)", flush=True)
	print(f"Chat model: {chat_model} | OCR model: {ocr_model}", flush=True)
	print(f"Bắt đầu từ Page {start_page}, ghi nối tiếp vào: {output_path}", flush=True)
	if not skip_ocr_images:
		print(f"Ảnh OCR → {assets_dir}", flush=True)

	session_last_page_text: str | None = None
	processed_count = 0

	for index in range(start_page, page_total + 1):
		print(f"[Trang {index}/{page_total}] Tách trang PDF...", flush=True)
		page_bytes = extract_page_pdf_bytes(pdf_path, index - 1)

		saved_images: list[str] = []
		if not skip_ocr_images:
			ocr_response = ocr_pdf_page(
				client,
				page_bytes,
				ocr_model=ocr_model,
				page_index=index,
				page_total=page_total,
			)
			ocr_pages = _get(ocr_response, "pages") or []
			page_images = _get(ocr_pages[0], "images") if ocr_pages else []
			saved_images = save_ocr_images(
				list(page_images or []),
				assets_dir,
				page_index=index,
			)
			if saved_images:
				print(
					f"[Trang {index}/{page_total}] Đã lưu {len(saved_images)} ảnh: "
					+ ", ".join(saved_images),
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
			page_total=page_total,
			saved_images=saved_images,
		)
		if last_question:
			question_num = extract_question_number(last_question)
			status = "chưa hoàn chỉnh" if was_incomplete else "đã hoàn chỉnh"
			label = f"Câu {question_num}" if question_num is not None else "câu cuối"
			print(
				f"[Trang {index}/{page_total}] Gửi kèm {label} ({status}) "
				f"({len(last_question)} ký tự).",
				flush=True,
			)

		text = extract_page_with_chat(
			client,
			page_bytes,
			page_prompt,
			chat_model=chat_model,
			page_index=index,
			page_total=page_total,
			has_last_context=last_question is not None,
		)
		text = rewrite_img_refs(text, saved_images, index)

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
		f"Hoàn tất {processed_count} trang (Page {start_page}→{page_total}) → {output_path}",
		flush=True,
	)


def main() -> int:
	parser = argparse.ArgumentParser(
		description="OCR PDF bằng Mistral Document QnA → text (prompt-mistral.md)"
	)
	parser.add_argument(
		"pdf",
		nargs="?",
		default=str(DEFAULT_PDF_PATH),
		help="Đường dẫn file PDF đầu vào",
	)
	parser.add_argument(
		"-o",
		"--output",
		default=str(DEFAULT_OUTPUT_TEXT_PATH),
		help="Đường dẫn file văn bản đầu ra",
	)
	parser.add_argument(
		"--model",
		default=DEFAULT_CHAT_MODEL,
		help="Model chat Document QnA (mặc định: mistral-small-latest)",
	)
	parser.add_argument(
		"--ocr-model",
		default=DEFAULT_OCR_MODEL,
		help="Model OCR để tách ảnh (mặc định: mistral-ocr-latest)",
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
		help="Trang bắt đầu (bỏ qua hỏi tương tác).",
	)
	parser.add_argument(
		"--skip-ocr-images",
		action="store_true",
		help="Bỏ bước OCR tách ảnh (chỉ chat Document QnA).",
	)
	args = parser.parse_args()

	pdf_path = Path(args.pdf).expanduser().resolve()
	output_path = Path(args.output).expanduser().resolve()
	prompt_path = Path(args.prompt).expanduser().resolve()

	try:
		prompt = load_prompt(prompt_path)
		print(f"Đã load prompt từ: {prompt_path}", flush=True)
		pdf_to_text(
			pdf_path,
			output_path,
			prompt,
			chat_model=args.model,
			ocr_model=args.ocr_model,
			start_page=args.start_page,
			skip_ocr_images=args.skip_ocr_images,
		)
		return 0
	except Exception as exc:  # noqa: BLE001
		print(f"Lỗi: {exc}", file=sys.stderr)
		return 1


if __name__ == "__main__":
	raise SystemExit(main())
