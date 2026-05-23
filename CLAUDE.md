# CLAUDE.md — mir-guide project conventions

## Package manager
- **uv** — `uv sync` to install; `uv run <cmd>` optional but `python` direct is fine after sync

## Language & tooling
- Python 3.11+
- Lint/format: **ruff** (line-length 100). Run `ruff check .` and `ruff format .` before committing.
- Validation: **pydantic v2**
- Templating: **jinja2**
- YAML parsing: **pyyaml**
- Type hints everywhere; docstrings on public functions; prefer pathlib over os.path

## Repository layout
```
data/           YAML source files, one per category
schema/         Generated JSON Schema (resource.schema.json)
scripts/        Python scripts (models.py, build_readme.py, export_schema.py, extract_urls.py)
.github/        Workflows and issue/PR templates
README.template.md   Jinja2 template — source of truth for README structure
README.md            Generated output — do not edit by hand
```

## Data model
- Source of truth: `scripts/models.py` (Pydantic v2 `Resource` model)
- Each `data/*.yaml` is a list of `Resource` entries
- `added` and `verified` dates use ISO-8601 format (YYYY-MM-DD)

## Build
- `python scripts/build_readme.py` — validate YAML and render README.md
- `python scripts/build_readme.py --check` — validate only, no file write
- `python scripts/export_schema.py` — regenerate schema/resource.schema.json

## Commit style
Conventional commits: `feat:`, `chore:`, `docs:`, `ci:`, `fix:`

## PR discipline
Each task is its own PR. Branch naming: `feat/task-N-short-description`.
