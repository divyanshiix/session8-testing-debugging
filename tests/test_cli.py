from pathlib import Path

from pytest import CaptureFixture, LogCaptureFixture

from session8_app.cli import run


def test_cli_with_numbers_argument(capsys: CaptureFixture[str]) -> None:
    exit_code = run(["--numbers", "1,2,3"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert '"average": 2.0' in output


def test_cli_with_input_file(tmp_path: Path, capsys: CaptureFixture[str]) -> None:
    file_path = tmp_path / "numbers.txt"
    file_path.write_text("2,4", encoding="utf-8")

    exit_code = run(["--input-file", str(file_path), "--pretty"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert output.startswith("{\n")
    assert '"sum": 6.0' in output


def test_cli_with_missing_input_returns_error(caplog: LogCaptureFixture) -> None:
    exit_code = run([])

    assert exit_code == 1
    assert "Provide --numbers" in caplog.text
