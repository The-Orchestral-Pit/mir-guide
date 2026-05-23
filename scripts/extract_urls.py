"""Print one URL per line from all data/*.yaml files."""

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent


def main() -> None:
    """Extract and print all resource URLs from the data directory."""
    for path in sorted((REPO_ROOT / "data").glob("*.yaml")):
        entries: list[dict] = yaml.safe_load(path.read_text()) or []
        for entry in entries:
            if url := entry.get("url"):
                print(url)


if __name__ == "__main__":
    main()
