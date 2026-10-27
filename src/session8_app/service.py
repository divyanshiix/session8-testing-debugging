"""Business logic for number parsing and analysis."""

from __future__ import annotations

from collections.abc import Iterable

from .errors import ValidationError


def parse_numbers(raw: str) -> list[float]:
    """Parse a comma-separated number string into floats."""
    values = [item.strip() for item in raw.split(",") if item.strip()]
    if not values:
        raise ValidationError("No numbers were provided.")

    parsed: list[float] = []
    for value in values:
        try:
            parsed.append(float(value))
        except ValueError as exc:
            raise ValidationError(f"Invalid number value: {value}") from exc
    return parsed


def analyze_numbers(numbers: Iterable[float]) -> dict[str, float]:
    """Compute summary statistics from numeric input."""
    data = list(numbers)
    if not data:
        raise ValidationError("At least one number is required for analysis.")

    total = sum(data)
    count = len(data)

    return {
        "count": float(count),
        "sum": total,
        "min": min(data),
        "max": max(data),
        "average": total / count,
    }
