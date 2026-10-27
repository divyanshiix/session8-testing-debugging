"""Configuration handling for environment-driven settings."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    """Runtime configuration loaded from environment variables."""

    log_level: str = "INFO"
    default_numbers: str = ""
    input_file: str = ""

    @classmethod
    def from_env(cls) -> AppConfig:
        return cls(
            log_level=os.getenv("SESSION8_LOG_LEVEL", "INFO").upper(),
            default_numbers=os.getenv("SESSION8_DEFAULT_NUMBERS", ""),
            input_file=os.getenv("SESSION8_INPUT_FILE", ""),
        )
