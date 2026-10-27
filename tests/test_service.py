import pytest

from session8_app.errors import ValidationError
from session8_app.service import analyze_numbers, parse_numbers


def test_parse_numbers_success() -> None:
    assert parse_numbers("1, 2.5,3") == [1.0, 2.5, 3.0]


def test_parse_numbers_rejects_invalid_value() -> None:
    with pytest.raises(ValidationError, match="Invalid number value"):
        parse_numbers("1,hello,3")


def test_parse_numbers_rejects_empty_input() -> None:
    with pytest.raises(ValidationError, match="No numbers were provided"):
        parse_numbers("   , ")


def test_analyze_numbers_success() -> None:
    result = analyze_numbers([1.0, 2.0, 3.0])
    assert result == {
        "count": 3.0,
        "sum": 6.0,
        "min": 1.0,
        "max": 3.0,
        "average": 2.0,
    }


def test_analyze_numbers_rejects_empty_iterable() -> None:
    with pytest.raises(ValidationError, match="At least one number"):
        analyze_numbers([])
