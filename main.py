#!/usr/bin/env python3
"""CLI chọn và chạy các tool trong core/.

Usage:
  python main.py                  # menu tương tác
  python main.py list             # liệt kê lệnh
  python main.py capture -- --dpi 150
  python main.py local -- --start-page 8
  python main.py ollama -- --model glm-ocr
  python main.py nvidia -- --start-page 1
  python main.py proxy -- --model minimax-m3
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Command:
	key: str
	aliases: tuple[str, ...]
	label: str
	description: str
	script: Path

	@property
	def names(self) -> tuple[str, ...]:
		return (self.key, *self.aliases)


COMMANDS: tuple[Command, ...] = (
	Command(
		key="capture",
		aliases=("cap", "pdf"),
		label="Capture PDF → ảnh",
		description="Chuyển trang PDF sang PNG (core/capture/capture.py)",
		script=PROJECT_ROOT / "core" / "capture" / "capture.py",
	),
	Command(
		key="local",
		aliases=("lm", "local-script"),
		label="OCR qua LM Studio",
		description="OCR ảnh bằng LM Studio / OpenAI-compatible (core/local-script.py)",
		script=PROJECT_ROOT / "core" / "local-script.py",
	),
	Command(
		key="ollama",
		aliases=("script", "ocr"),
		label="OCR qua Ollama",
		description="OCR ảnh bằng Ollama (core/script.py)",
		script=PROJECT_ROOT / "core" / "script.py",
	),
	Command(
		key="nvidia",
		aliases=("nv", "minimax"),
		label="OCR qua NVIDIA",
		description="OCR ảnh bằng NVIDIA API / MiniMax-M3 (core/nvidia.py)",
		script=PROJECT_ROOT / "core" / "nvidia.py",
	),
	Command(
		key="proxy",
		aliases=("px", "servernvidia"),
		label="OCR qua servernvidia proxy",
		description="OCR ảnh qua proxy local OpenAI-compatible (core/proxy.py)",
		script=PROJECT_ROOT / "core" / "proxy.py",
	),
)


def find_command(name: str) -> Command | None:
	needle = name.strip().lower()
	for cmd in COMMANDS:
		if needle in cmd.names:
			return cmd
	return None


def print_commands() -> None:
	print("Các lệnh có sẵn:\n")
	for index, cmd in enumerate(COMMANDS, start=1):
		alias_text = ", ".join(cmd.aliases)
		print(f"  {index}. {cmd.key:<10}  {cmd.label}")
		print(f"     {cmd.description}")
		if alias_text:
			print(f"     alias: {alias_text}")
		print()


def run_command(cmd: Command, extra_args: list[str]) -> int:
	if not cmd.script.is_file():
		print(f"Lỗi: không tìm thấy script {cmd.script}", file=sys.stderr)
		return 1

	argv = [sys.executable, str(cmd.script), *extra_args]
	print(f"→ Chạy: {' '.join(argv)}\n", flush=True)
	try:
		completed = subprocess.run(argv, cwd=PROJECT_ROOT, check=False)
	except KeyboardInterrupt:
		print("\nĐã hủy.", file=sys.stderr)
		return 130
	return int(completed.returncode)


def interactive_menu() -> int:
	print("=" * 48)
	print("  ML Tools CLI")
	print("=" * 48)
	print()
	print_commands()
	print("  0. Thoát")
	print()

	while True:
		try:
			choice = input("Chọn lệnh (số hoặc tên) > ").strip()
		except (EOFError, KeyboardInterrupt):
			print()
			return 0

		if not choice or choice in {"0", "q", "quit", "exit"}:
			return 0

		cmd: Command | None = None
		if choice.isdigit():
			index = int(choice)
			if 1 <= index <= len(COMMANDS):
				cmd = COMMANDS[index - 1]
		else:
			cmd = find_command(choice)

		if cmd is None:
			print("Lựa chọn không hợp lệ. Thử lại.\n")
			continue

		print(f"\nĐã chọn: {cmd.label}")
		print("Nhập thêm args cho script (Enter = mặc định).")
		print("Ví dụ: --dpi 150   hoặc   -o .md/out.md --start-page 8")
		try:
			raw = input("Args > ").strip()
		except (EOFError, KeyboardInterrupt):
			print()
			return 0

		extra_args = raw.split() if raw else []
		return run_command(cmd, extra_args)


def build_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(
		prog="main.py",
		description="CLI chọn và chạy các tool trong core/",
		formatter_class=argparse.RawDescriptionHelpFormatter,
		epilog=(
			"Ví dụ:\n"
			"  python main.py\n"
			"  python main.py list\n"
			"  python main.py capture -- input.pdf -o rawtext/_preview_pages1\n"
			"  python main.py local -- --start-page 8 -o .md/out.md\n"		"  python main.py local -- --local-model local-model --proxy-model minimax-m3\n"			"  python main.py ollama -- --model glm-ocr\n"
			"  python main.py nvidia -- --start-page 1 -o .md/out.md\n"
			"  python main.py proxy -- --model minimax-m3 --start-page 1\n"
		),
	)
	sub = parser.add_subparsers(dest="action")

	sub.add_parser("list", help="Liệt kê các lệnh có sẵn")
	sub.add_parser("menu", help="Mở menu tương tác")
	for cmd in COMMANDS:
		p = sub.add_parser(
			cmd.key,
			aliases=list(cmd.aliases),
			help=cmd.label,
			description=cmd.description,
		)
		p.add_argument(
			"script_args",
			nargs=argparse.REMAINDER,
			help="Args truyền tiếp cho script (thường sau --)",
		)

	return parser


def normalize_passthrough(args: list[str]) -> list[str]:
	"""Bỏ dấu '--' đầu nếu người dùng dùng dạng: main.py capture -- --dpi 150."""
	if args and args[0] == "--":
		return args[1:]
	return args


def main(argv: list[str] | None = None) -> int:
	parser = build_parser()
	args = parser.parse_args(argv)

	if args.action is None:
		return interactive_menu()

	if args.action == "list":
		print_commands()
		return 0

	if args.action == "menu":
		return interactive_menu()

	cmd = find_command(args.action)
	if cmd is None:
		parser.error(f"Không tìm thấy lệnh: {args.action}")

	extra = normalize_passthrough(getattr(args, "script_args", []) or [])
	return run_command(cmd, extra)


if __name__ == "__main__":
	raise SystemExit(main())
