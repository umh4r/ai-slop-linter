"""コマンドラインエントリポイント。"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from ai_slop_linter import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ai-slop-linter",
        description="日本語文書を校正 lint する。",
    )
    parser.add_argument("paths", nargs="*", help="対象ファイル")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.paths:
        parser.print_usage(sys.stderr)
        return 2
    # TODO: ルールを実装して各ファイルを検査する。
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
