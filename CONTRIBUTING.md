# Contributing

## Setup

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -e .[dev]`.
3. Run `pre-commit install` (optional but recommended).

## Local checks

Run before opening a PR:

```bash
black --check .
ruff check .
mypy src tests
pytest
```

## Scope

Keep changes small, tested, and documented.
