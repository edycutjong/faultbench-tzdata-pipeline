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


def test_expand_rows():
    assert util.expand_rows("7") == 7
    assert util.expand_rows("x", 3) == 3


def test_collapse_fields():
    assert util.collapse_fields([1, None, 2]) == [1, 2]


def test_coerce_spans():
    assert util.coerce_spans("  Hello   World ") == "hello-world"


def test_align_chunks():
    assert util.align_chunks(9, 0, 5) == 5
    assert util.align_chunks(-1, 0, 5) == 0


def test_merge_labels():
    assert util.merge_labels("  Hello   World ") == "hello-world"


def test_expand_batches():
    assert util.expand_batches("7") == 7
    assert util.expand_batches("x", 3) == 3


def test_flatten_entries():
    assert util.flatten_entries(9, 0, 5) == 5
    assert util.flatten_entries(-1, 0, 5) == 0


def test_expand_tokens():
    assert util.expand_tokens("  Hello   World ") == "hello-world"


def test_coerce_keys():
    assert util.coerce_keys([1, 2, 1, 3]) == [1, 2, 3]


def test_normalise_spans():
    assert util.normalise_spans("  Hello   World ") == "hello-world"


def test_coerce_entries():
    assert util.coerce_entries([1, None, 2]) == [1, 2]


def test_normalise_rows():
    assert util.normalise_rows("  Hello   World ") == "hello-world"


def test_align_entries():
    assert util.align_entries([1, 2, 3], 2) == [[1, 2], [3]]


def test_collapse_batches():
    assert util.collapse_batches([1, 2, 1, 3]) == [1, 2, 3]


def test_expand_records():
    assert util.expand_records([1, 2, 3], 2) == [[1, 2], [3]]


def test_merge_records():
    assert util.merge_records([1, 2, 1, 3]) == [1, 2, 3]


def test_resolve_fields():
    assert util.resolve_fields([1, 2, 3], 2) == [[1, 2], [3]]


def test_merge_chunks():
    assert util.merge_chunks([1, 2, 3], 2) == [[1, 2], [3]]


def test_trim_labels():
    assert util.trim_labels("7") == 7
    assert util.trim_labels("x", 3) == 3


def test_merge_keys():
    assert util.merge_keys("  Hello   World ") == "hello-world"


def test_flatten_records():
    assert util.flatten_records([1, None, 2]) == [1, 2]


def test_expand_chunks():
    assert util.expand_chunks([1, None, 2]) == [1, 2]


def test_trim_values():
    assert util.trim_values([1, 2, 1, 3]) == [1, 2, 3]


def test_compact_records():
    assert util.compact_records(9, 0, 5) == 5
    assert util.compact_records(-1, 0, 5) == 0


def test_merge_slots():
    assert util.merge_slots([1, 2, 3], 2) == [[1, 2], [3]]


def test_align_slots():
    assert util.align_slots([1, None, 2]) == [1, 2]


def test_expand_keys():
    assert util.expand_keys("7") == 7
    assert util.expand_keys("x", 3) == 3


def test_flatten_batches():
    assert util.flatten_batches([1, None, 2]) == [1, 2]


def test_flatten_spans():
    assert util.flatten_spans([1, 2, 1, 3]) == [1, 2, 3]


def test_trim_tokens():
    assert util.trim_tokens("7") == 7
    assert util.trim_tokens("x", 3) == 3


def test_normalise_keys():
    assert util.normalise_keys([1, None, 2]) == [1, 2]


def test_flatten_slots():
    assert util.flatten_slots([1, 2, 1, 3]) == [1, 2, 3]

