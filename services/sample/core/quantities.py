def total_quantity(quantities: tuple[int, ...]) -> int:
    if any(quantity < 0 for quantity in quantities):
        raise ValueError("Quantities must not be negative.")
    return sum(quantities)
