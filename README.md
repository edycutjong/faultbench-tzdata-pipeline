# tzdata-pipeline

Normalise event timestamps arriving from mixed-offset feeds.

> **This is a FAULTBENCH fixture.** Its whole history is generated, deterministically, by
> `scripts/seed.py` in [Faultline](https://github.com/edycutjong/faultline) so that a
> bisection tool can be checked against a known answer. The answer key is not in this
> repository.

## Install

    pip install -e .[test]

## Test

    python -m pytest -q

## Usage notes

- Everything in this package is pure and side-effect free; the tests need no fixtures.
- The public surface is re-exported from `tzdata_pipeline/__init__.py`.
- State the precision the caller can count on.
- Cross-reference the module that owns this contract.
- Explain the naming of the private helpers.
- Flag the branch that is deliberately not defensive.
- State the precision the caller can count on.
- Flag the branch that is deliberately not defensive.
- Record why the offset table is hand-maintained.
