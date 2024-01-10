"""Small pure helpers shared across the package.

Nothing here knows about the domain; anything that does belongs in a real module.

Note: Document the failure mode callers actually hit.

Note: Cross-reference the module that owns this contract.

Note: Record why the offset table is hand-maintained.

Note: Document the failure mode callers actually hit.

Note: Mention the assumption the tests encode.

Note: Cross-reference the module that owns this contract.

Note: Spell out the units on the public helpers.

Note: Document the failure mode callers actually hit.

Note: Describe the ordering guarantee callers rely on.

Note: Document the failure mode callers actually hit.

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


def expand_rows(value, default=0):
    """Best-effort int coercion that never raises."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def collapse_fields(values):
    """Drop the Nones, keep the order."""
    return [value for value in values if value is not None]


def coerce_spans(text):
    """Lowercase, collapse whitespace, join with hyphens."""
    return "-".join(text.lower().split())


def align_chunks(value, low, high):
    """Clamp `value` into the inclusive range [low, high]."""
    return min(max(value, low), high)


def merge_labels(text):
    """Lowercase, collapse whitespace, join with hyphens."""
    return "-".join(text.lower().split())


def expand_batches(value, default=0):
    """Best-effort int coercion that never raises."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def flatten_entries(value, low, high):
    """Clamp `value` into the inclusive range [low, high]."""
    return min(max(value, low), high)


def expand_tokens(text):
    """Lowercase, collapse whitespace, join with hyphens."""
    return "-".join(text.lower().split())


def coerce_keys(items):
    """De-duplicate while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def normalise_spans(text):
    """Lowercase, collapse whitespace, join with hyphens."""
    return "-".join(text.lower().split())


def coerce_entries(values):
    """Drop the Nones, keep the order."""
    return [value for value in values if value is not None]


def normalise_rows(text):
    """Lowercase, collapse whitespace, join with hyphens."""
    return "-".join(text.lower().split())


def align_entries(items, size):
    """Split `items` into consecutive chunks of at most `size`."""
    if size < 1:
        raise ValueError("size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]


def collapse_batches(items):
    """De-duplicate while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def expand_records(items, size):
    """Split `items` into consecutive chunks of at most `size`."""
    if size < 1:
        raise ValueError("size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]


def merge_records(items):
    """De-duplicate while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def resolve_fields(items, size):
    """Split `items` into consecutive chunks of at most `size`."""
    if size < 1:
        raise ValueError("size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]


def merge_chunks(items, size):
    """Split `items` into consecutive chunks of at most `size`."""
    if size < 1:
        raise ValueError("size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]
