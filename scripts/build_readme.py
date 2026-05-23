"""Build README.md from the Jinja2 template and YAML data files."""

import argparse
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from models import Resource
from pydantic import ValidationError

REPO_ROOT = Path(__file__).parent.parent

DATA_FILES = {
    "communities": REPO_ROOT / "data" / "communities.yaml",
    "events": REPO_ROOT / "data" / "events.yaml",
    "labs": REPO_ROOT / "data" / "labs.yaml",
    "newsletters": REPO_ROOT / "data" / "newsletters.yaml",
    "podcasts": REPO_ROOT / "data" / "podcasts.yaml",
    "blogs": REPO_ROOT / "data" / "blogs.yaml",
    "learning": REPO_ROOT / "data" / "learning.yaml",
    "related_lists": REPO_ROOT / "data" / "related-lists.yaml",
}


def load_and_validate(path: Path) -> list[Resource]:
    """Load a YAML data file and validate every entry against the Resource model."""
    raw: list[dict] = yaml.safe_load(path.read_text())
    resources: list[Resource] = []
    errors: list[str] = []

    for i, entry in enumerate(raw):
        try:
            resources.append(Resource(**entry))
        except ValidationError as exc:
            name = entry.get("name", f"entry[{i}]")
            errors.append(f"  {path.name} / {name}:\n    {exc}")

    if errors:
        print("Validation errors found:")
        print("\n".join(errors))
        sys.exit(1)

    return resources


def group_by_attr(resources: list[Resource], attr: str) -> dict[str, list[Resource]]:
    """Partition resources into an ordered dict keyed by the given attribute value.

    Entries where the attribute is None are collected under the key "other".
    Insertion order follows the order items appear in the source list.
    """
    groups: dict[str, list[Resource]] = defaultdict(list)
    for r in resources:
        val = getattr(r, attr)
        key = str(val) if val is not None else "other"
        groups[key].append(r)
    return dict(groups)


def main() -> None:
    """Entry point: validate data and optionally render README.md."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate only; skip rendering.")
    args = parser.parse_args()

    data: dict[str, list[Resource]] = {}
    for key, path in DATA_FILES.items():
        data[key] = load_and_validate(path)

    total = sum(len(v) for v in data.values())

    if args.check:
        print(f"OK — {total} entries validated across {len(DATA_FILES)} files.")
        return

    labs_by_region = group_by_attr(data["labs"], "region")
    events_by_type = group_by_attr(data["events"], "event_type")

    env = Environment(
        loader=FileSystemLoader(str(REPO_ROOT)),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("README.template.md")
    rendered = template.render(
        **data,
        labs_by_region=labs_by_region,
        events_by_type=events_by_type,
        build_date=date.today().isoformat(),
    )

    out = REPO_ROOT / "README.md"
    out.write_text(rendered)
    print(f"Wrote {out} ({total} entries)")


if __name__ == "__main__":
    main()
