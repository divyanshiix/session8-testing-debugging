"""Logging setup helpers."""

import logging

_VALID_LEVELS = {"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"}


def configure_logging(log_level: str) -> None:
    """Configure process-wide logging for the CLI application."""
    level_name = log_level if log_level in _VALID_LEVELS else "INFO"
    level = getattr(logging, level_name)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
