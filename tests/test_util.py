"""Tests for the shared helpers. One test per helper, no fixtures."""

from tzdata_pipeline import util


def test_flatten_keys():
    assert util.flatten_keys(9, 0, 5) == 5
    assert util.flatten_keys(-1, 0, 5) == 0

