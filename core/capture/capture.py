"""Chuyển tất cả trang PDF sang ảnh PNG trong folder preview_pages.

Usage:
  python core/capture/capture.py
  python core/capture/capture.py input.pdf
  python core/capture/capture.py input.pdf -o rawtext/preview_pages
  python core/capture/capture.py input.pdf --dpi 150
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from pdf2image import convert_from_path  # pyright: ignore[reportMissingImports]


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_INPUT_PDF_PATH = PROJECT_ROOT / "rawtext" / "MMT-IT3080-CK20221_231.pdf"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "rawtext" / "_preview_pages1"
DEFAULT_DPI = 220
DEFAULT_POPPLER_PATH = None


def pdf_to_images(
	pdf_path: Path,
	output_dir: Path,
	dpi: int,
	poppler_path: str | None,
) -> int:
	if not pdf_path.exists():
		raise FileNotFoundError(f"Không tìm thấy file PDF: {pdf_path}")

	output_dir.mkdir(parents=True, exist_ok=True)

	print(f"Đang chuyển PDF sang ảnh (dpi={dpi})...", flush=True)
	started = time.monotonic()
	images = convert_from_path(
		str(pdf_path),
		dpi=dpi,
		fmt="png",
		poppler_path=poppler_path,
	)
	elapsed = time.monotonic() - started

	if not images:
		raise RuntimeError("Không chuyển được trang nào từ PDF sang ảnh")

	page_total = len(images)
	for index, image in enumerate(images, start=1):
		image_path = output_dir / f"page_{index:04d}.png"
		print(f"[Trang {index}/{page_total}] Đang lưu {image_path.name}...", flush=True)
		image.save(image_path, format="PNG")

	print(
		f"Hoàn tất: {page_total} trang → {output_dir} ({elapsed:.1f}s)",
		flush=True,
	)
	return page_total


def main() -> int:
	parser = argparse.ArgumentParser(
		description="Chuyển tất cả trang PDF sang ảnh PNG"
	)
	parser.add_argument(
		"pdf",
		nargs="?",
		default=str(DEFAULT_INPUT_PDF_PATH),
		help="Đường dẫn file PDF đầu vào",
	)
	parser.add_argument(
		"-o",
		"--output",
		default=str(DEFAULT_OUTPUT_DIR),
		help="Thư mục lưu ảnh đầu ra",
	)
	parser.add_argument(
		"--dpi",
		type=int,
		default=DEFAULT_DPI,
		help="Độ phân giải khi chuyển PDF sang ảnh",
	)
	parser.add_argument(
		"--poppler-path",
		default=DEFAULT_POPPLER_PATH,
		help="Đường dẫn poppler nếu pdf2image không tự tìm thấy",
	)
	args = parser.parse_args()

	pdf_path = Path(args.pdf).expanduser().resolve()
	output_dir = Path(args.output).expanduser().resolve()

	try:
		pdf_to_images(pdf_path, output_dir, args.dpi, args.poppler_path)
		return 0
	except Exception as exc:  # noqa: BLE001
		print(f"Lỗi: {exc}", file=sys.stderr)
		return 1


if __name__ == "__main__":
	raise SystemExit(main())
