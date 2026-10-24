import json
import sys

from services.sample.core.quantities import total_quantity


def parse_request(payload: object) -> tuple[int, ...]:
    if not isinstance(payload, dict) or set(payload) != {"quantities"}:
        raise ValueError("Expected only the quantities field.")
    quantities = payload["quantities"]
    if not isinstance(quantities, list):
        raise ValueError("Quantities must be an array.")
    if any(type(quantity) is not int for quantity in quantities):
        raise ValueError("Quantities must contain integers.")
    return tuple(quantities)


def main() -> int:
    try:
        quantities = parse_request(json.load(sys.stdin))
        result = total_quantity(quantities)
    except (ValueError, TypeError, RecursionError):
        print("Invalid quantity request.", file=sys.stderr)
        return 2
    print(json.dumps({"total": result}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
