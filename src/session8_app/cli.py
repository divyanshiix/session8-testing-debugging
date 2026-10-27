"""CLI entrypoint for the session8 number analyzer."""

from __future__ import annotations

import argparse
import json
import logging
import sys

from .config import AppConfig
from .errors import AppError, ValidationError
from .logging_utils import configure_logging
from .repository import load_numbers_from_file
from .service import analyze_numbers, parse_numbers

LOGGER = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze comma-separated numeric input."
    )
    parser.add_argument(
        "--numbers",
        help="Comma-separated numbers to analyze (e.g. '1,2,3.5').",
    )
    parser.add_argument(
        "--input-file",
        help="Text file containing comma-separated numbers.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output.",
    )
    return parser


def resolve_raw_input(args: argparse.Namespace, config: AppConfig) -> str:
    numbers_arg = getattr(args, "numbers", None)
    if isinstance(numbers_arg, str) and numbers_arg:
        return numbers_arg

    input_file_arg = getattr(args, "input_file", None)
    if isinstance(input_file_arg, str) and input_file_arg:
        return load_numbers_from_file(input_file_arg)

    if config.input_file:
        return load_numbers_from_file(config.input_file)
    if config.default_numbers:
        return config.default_numbers
    raise ValidationError(
        "Provide --numbers, --input-file, SESSION8_INPUT_FILE, "
        "or SESSION8_DEFAULT_NUMBERS."
    )


def run(argv: list[str] | None = None) -> int:
    config = AppConfig.from_env()
    configure_logging(config.log_level)

    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        raw = resolve_raw_input(args, config)
        results = analyze_numbers(parse_numbers(raw))
    except AppError as exc:
        LOGGER.error("%s", exc)
        return 1

    indent = 2 if args.pretty else None
    print(json.dumps(results, indent=indent, sort_keys=True))
    return 0


def main() -> None:
    sys.exit(run())


if __name__ == "__main__":
    main()
