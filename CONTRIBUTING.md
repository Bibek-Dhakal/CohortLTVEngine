# Contributing to CohortLTV-Engine

Thank you for your interest in contributing! This project follows strict guidelines to maintain code quality, robust documentation, and automated versioning.

## Development Workflow

1. **Clone & Setup:** Clone the repository and run `pip install -e .[dev]` to install dependencies.
2. **Pre-commit Hooks:** Run `pre-commit install` to ensure code quality checks run automatically before you commit.
3. **Branching:** Create a feature branch (`feature/description`, `fix/issue-name`).
4. **Testing:** Run tests via `pytest` before submitting a PR.

## Commit Message Standards (Strict)

This repository uses [Release Please](https://github.com/googleapis/release-please) for automated versioning and changelog generation. **All commit messages must follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.**

Format: `<type>(<optional scope>): <description>`

### Allowed Types:
* `feat:` A new feature (triggers a MINOR release).
* `fix:` A bug fix (triggers a PATCH release).
* `feat!:` or `fix!:` A breaking change (triggers a MAJOR release).
* `docs:` Documentation only changes.
* `style:` Changes that do not affect the meaning of the code (white-space, formatting, etc).
* `refactor:` A code change that neither fixes a bug nor adds a feature.
* `perf:` A code change that improves performance.
* `test:` Adding missing tests or correcting existing tests.
* `chore:` Changes to the build process or auxiliary tools and libraries.

*Note: The PR title must also adhere to this format as it is often used as the squash merge commit message.*

## Release Process

We use a managed Release PR workflow.
1. When conventional commits are merged to `main`, `release-please` automatically opens or updates a draft Release PR.
2. The Release PR tracks unreleased changes.
3. When the maintainer merges the Release PR, an official release tag is created, and the `CHANGELOG.md` is updated.
