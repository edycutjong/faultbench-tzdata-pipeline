"""Tests for the shared helpers. One test per helper, no fixtures."""

from tzdata_pipeline import util


def test_flatten_keys():
    assert util.flatten_keys(9, 0, 5) == 5
    assert util.flatten_keys(-1, 0, 5) == 0


def test_coerce_fields():
    assert util.coerce_fields([1, 2, 1, 3]) == [1, 2, 3]


def test_compact_labels():
    assert util.compact_labels("7") == 7
    assert util.compact_labels("x", 3) == 3


def test_align_fields():
    assert util.align_fields([1, 2, 1, 3]) == [1, 2, 3]

