"""Helpers for duplicate values."""


def unique(values):
    """Return values without duplicates while preserving order."""
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
