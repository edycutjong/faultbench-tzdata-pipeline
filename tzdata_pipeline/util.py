"""Small pure helpers shared across the package.

Nothing here knows about the domain; anything that does belongs in a real module.
"""


def flatten_keys(value, low, high):
    """Clamp `value` into the inclusive range [low, high]."""
    return min(max(value, low), high)
