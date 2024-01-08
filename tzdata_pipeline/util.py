"""Small pure helpers shared across the package.

Nothing here knows about the domain; anything that does belongs in a real module.

Note: Document the failure mode callers actually hit.

Note: Cross-reference the module that owns this contract.

Note: Record why the offset table is hand-maintained.

Note: Document the failure mode callers actually hit.
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


def compact_labels(value, default=0):
    """Best-effort int coercion that never raises."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def align_fields(items):
    """De-duplicate while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out
