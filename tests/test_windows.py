"""Tests for fixed-width windowing."""

from datetime import datetime, timezone

import pytest

from tzdata_pipeline.windows import floor_to, window_key


def test_floor_to_rounds_down_to_the_window():
    moment = datetime(2024, 3, 1, 12, 47, 31, tzinfo=timezone.utc)
    assert floor_to(moment, 15) == datetime(2024, 3, 1, 12, 45, tzinfo=timezone.utc)


def test_floor_to_rejects_a_zero_window():
    with pytest.raises(ValueError):
        floor_to(datetime(2024, 3, 1, tzinfo=timezone.utc), 0)


def test_window_key_is_rendered_in_local_time():
    moment = datetime(2024, 3, 1, 12, 47, tzinfo=timezone.utc)
    assert window_key(moment, "Asia/Jakarta", 15) == "2024-03-01T19:45+0700"
