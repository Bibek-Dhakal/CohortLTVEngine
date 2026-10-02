# Code Quality Standards

This project uses modern automated tooling to ensure code consistency and prevent bugs. Quality checks are integrated
automatically via `pre-commit` hooks.

## Environment Setup

To ensure quality tools run automatically before you commit:

```bash
# 1. Install development dependencies
pip install -e .[dev]

# 2. Register git hooks
pre-commit install
```

Automated quality checks now run automatically on `git commit`.

## Tooling Used

- **Ruff**: Extremely fast Python linter and formatter (replaces Black, isort, Flake8).
- **Commitlint**: Validates conventional commit messages.

## Manual Execution Commands

Run all checks repository-wide on ALL files:

```bash
pre-commit run --all-files
```

Run checks ONLY on staged files:

```bash
pre-commit run
```

Run specific tools independently:

```bash
# Format code
ruff format .

# Run linter and auto-fix minor issues
ruff check . --fix
```

## Emergency Bypassing

If you absolutely must bypass the checks (e.g., hotfixing an issue quickly), append the bypass flag to your git commit
command:

```bash
git commit -m "fix(urgent): patch issue" --no-verify
```

*Warning: Use bypasses sparingly and responsibly.*
