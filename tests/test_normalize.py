"""Tests for offset normalisation.

`test_naive_local_midnight_is_interpreted_in_zone` is the one that pins the contract
for the legacy CSV feed: naive input means local wall-clock in that zone, under the
zone rules of the pinned tz database (see pyproject.toml).
"""

from datetime import datetime, timedelta, timezone

import pytest

from tzdata_pipeline.normalize import ZONES, day_bucket, offset_minutes, parse_iso, to_utc, zone_for


def test_zone_table_covers_the_documented_zones():
    assert set(ZONES) == {
        "UTC",
        "Europe/Amsterdam",
        "Asia/Jakarta",
        "Asia/Tokyo",
        "America/New_York",
        "America/Mexico_City",
    }


def test_zone_for_rejects_an_unknown_zone():
    with pytest.raises(ValueError):
        zone_for("Mars/Olympus")


def test_aware_input_keeps_its_own_offset():
    aware = datetime(2024, 3, 1, 12, 0, tzinfo=timezone(timedelta(minutes=420)))
    assert to_utc(aware, "UTC") == datetime(2024, 3, 1, 5, 0, tzinfo=timezone.utc)


def test_naive_local_midnight_is_interpreted_in_zone():
    # Golden value for the pinned tz database: Mexico City observes daylight saving
    # time in July 2023, so local midnight is 05:00 UTC.
    naive = datetime(2023, 7, 1, 0, 0)
    assert to_utc(naive, "America/Mexico_City") == datetime(2023, 7, 1, 5, 0, tzinfo=timezone.utc)


def test_jakarta_has_no_daylight_saving():
    assert offset_minutes(datetime(2024, 7, 1, 12, 0), "Asia/Jakarta") == 420


def test_day_bucket_uses_the_local_calendar_date():
    aware = datetime(2024, 3, 1, 23, 30, tzinfo=timezone.utc)
    assert day_bucket(aware, "Asia/Jakarta") == "2024-03-02"


def test_parse_iso_accepts_trailing_z():
    assert parse_iso("2024-03-01T00:00:00Z") == datetime(2024, 3, 1, tzinfo=timezone.utc)
