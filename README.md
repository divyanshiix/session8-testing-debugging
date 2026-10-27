# session8-testing-debugging

A production-ready Python CLI that analyzes comma-separated numbers and returns summary statistics in JSON.

## Features

- Parse numeric input from CLI arguments, environment variables, or text files
- Compute count, sum, min, max, and average
- Validate bad/empty input with clear errors
- Logging and environment-driven configuration
- Quality tooling with pytest, Ruff, Black, and mypy

## Requirements

- Python 3.10+

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install --upgrade pip
pip install -e .[dev]
```

## Environment setup

Copy and edit the example:

```bash
cp .env.example .env
```

Supported variables:

- `SESSION8_LOG_LEVEL` (`DEBUG|INFO|WARNING|ERROR|CRITICAL`)
- `SESSION8_DEFAULT_NUMBERS` (fallback comma-separated values)
- `SESSION8_INPUT_FILE` (fallback file path for input)

## Run locally

```bash
session8-analyze --numbers "1,2,3"
# or
python -m session8_app.cli --input-file ./numbers.txt --pretty
```

## Tests and quality checks

```bash
pytest
ruff check .
black --check .
mypy src tests
```

## Example usage

```bash
session8-analyze --numbers "1,2,3"
```

Example output:

```json
{"average": 2.0, "count": 3.0, "max": 3.0, "min": 1.0, "sum": 6.0}
```

## Project structure

```text
src/session8_app/
  cli.py            # CLI entrypoint
  config.py         # environment-backed configuration
  errors.py         # typed application errors
  repository.py     # file input loader
  service.py        # parse and analysis business logic
tests/              # pytest suite
.github/workflows/ci.yml
```

## Troubleshooting

- If `session8-analyze` is not found, reinstall with `pip install -e .[dev]`.
- If you get `No numbers were provided`, ensure comma-separated numeric values are supplied.
- If file loading fails, verify `--input-file` path exists and is readable.

## Security notes

- No credentials are hardcoded.
- Configuration is environment-driven.
- Do not commit `.env` files or sensitive local data.

## License

No license has been selected yet.
