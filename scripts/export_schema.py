"""Generate schema/resource.schema.json from the Pydantic Resource model."""

import json
from pathlib import Path

from models import Resource


def main() -> None:
    """Export the Resource JSON Schema to schema/resource.schema.json."""
    schema = Resource.model_json_schema()
    out = Path(__file__).parent.parent / "schema" / "resource.schema.json"
    out.write_text(json.dumps(schema, indent=2) + "\n")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
