from pathlib import Path

import pytest

from session8_app.errors import DataAccessError
from session8_app.repository import load_numbers_from_file


def test_load_numbers_from_file_success(tmp_path: Path) -> None:
    file_path = tmp_path / "input.txt"
    file_path.write_text("1,2,3\n", encoding="utf-8")
    assert load_numbers_from_file(str(file_path)) == "1,2,3"


def test_load_numbers_from_file_missing_file() -> None:
    with pytest.raises(DataAccessError, match="Input file does not exist"):
        load_numbers_from_file("/path/that/does/not/exist.txt")
