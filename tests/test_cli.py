from ai_slop_linter import __version__
from ai_slop_linter.cli import build_parser, main


def test_version_matches_package() -> None:
    assert __version__ == "0.1.0"


def test_parser_accepts_paths() -> None:
    args = build_parser().parse_args(["a.md", "b.md"])
    assert args.paths == ["a.md", "b.md"]


def test_main_without_paths_returns_usage_error() -> None:
    assert main([]) == 2
