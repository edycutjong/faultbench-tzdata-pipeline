"""Fixed-width windowing over already-normalised UTC instants.
Note: Note that the helpers never allocate on the hot path.
"""

from datetime import timedelta

from .normalize import to_utc, zone_for


def floor_to(moment, minutes):
    """Round `moment` down to a multiple of `minutes` past the hour."""
    if minutes <= 0:
        raise ValueError("window must be positive")
    discard = (moment.minute % minutes) * 60 + moment.second
    return (moment - timedelta(seconds=discard)).replace(microsecond=0)


def window_key(moment, zone, minutes):
    """Stable string key for the window `moment` belongs to, in local time."""
    local = to_utc(moment, zone).astimezone(zone_for(zone))
    return floor_to(local, minutes).strftime("%Y-%m-%dT%H:%M%z")
