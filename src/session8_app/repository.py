"""Data access helpers."""

from __future__ import annotations

from pathlib import Path

from .errors import DataAccessError


def load_numbers_from_file(file_path: str) -> str:
    """Return raw number content from a text file."""
    path = Path(file_path)
    if not path.exists():
        raise DataAccessError(f"Input file does not exist: {file_path}")

    try:
        return path.read_text(encoding="utf-8").strip()
    except OSError as exc:  # pragma: no cover - platform-specific I/O failures
        raise DataAccessError(f"Unable to read input file: {file_path}") from exc
