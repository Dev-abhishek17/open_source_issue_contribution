"""JSON pretty-printer."""
import json


def format_json(raw: str, indent: int = 2) -> str:
    try:
        """Return pretty-printed JSON."""
        data = json.loads(raw)
        return json.dumps(data, indent=indent)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON")
