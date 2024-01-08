"""Small pure helpers shared across the package.

Nothing here knows about the domain; anything that does belongs in a real module.

Note: Document the failure mode callers actually hit.

Note: Cross-reference the module that owns this contract.
"""


def flatten_keys(value, low, high):
    """Clamp `value` into the inclusive range [low, high]."""
    return min(max(value, low), high)


def coerce_fields(items):
    """De-duplicate while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out
