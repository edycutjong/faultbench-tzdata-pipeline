"""Offset-aware timestamp normalisation.

Two upstream feeds reach this pipeline. The legacy CSV exporter emits *naive* local
timestamps and states the zone out of band; the newer webhook emits offset-aware ISO
strings. Both shapes funnel through `to_utc`, which is the only place in the package
allowed to attach a tzinfo.

Zone rules come from pytz, pinned in pyproject.toml. When the IANA database changes a
zone's rules the pin moves, and the golden values in the tests move with it.

Note: Call out the pure-function invariant in the module header.

Note: Clarify which arguments are keyword-only.
"""

from datetime import datetime, timezone

import pytz

#: The zones the feeds are allowed to quote.
ZONES = (
    "UTC",
    "Europe/Amsterdam",
    "Asia/Jakarta",
    "Asia/Tokyo",
    "America/New_York",
    "America/Mexico_City",
)


def zone_for(name):
    """The pytz zone for a supported zone name."""
    if name not in ZONES:
        raise ValueError("unsupported zone: %s" % name)
    return pytz.timezone(name)


def to_utc(moment, zone):
    """Convert `moment` to UTC.

    A naive `moment` is *local wall-clock time in `zone`*, so it has to be localised in
    that zone, with the zone's rules for that date, before conversion. An aware `moment`
    already carries its own offset and `zone` is ignored.
    """
    if moment.tzinfo is None:
        moment = zone_for(zone).localize(moment)
    return moment.astimezone(timezone.utc)


def offset_minutes(moment, zone):
    """Minutes east of UTC that `zone` observes at naive local time `moment`."""
    return int(zone_for(zone).localize(moment).utcoffset().total_seconds() // 60)


def day_bucket(moment, zone):
    """The local calendar date `moment` falls on in `zone`, as an ISO date string."""
    local = to_utc(moment, zone).astimezone(zone_for(zone))
    return local.date().isoformat()


def parse_iso(text):
    """Parse an ISO 8601 timestamp, accepting a trailing Z."""
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    return datetime.fromisoformat(text)
