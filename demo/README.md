# Demo — known-constant checker

A small, runnable tool that mechanizes the single check from this casebook that
genuinely automates (see [`../PROTOCOL.md`](../PROTOCOL.md) step 4 and
[Case 01](../case-studies/01-known-constant.md)):

> Given a value you computed, search whether it is secretly a re-expression of
> known published constants — and flag it if it is.

This is the [Case 01](../case-studies/01-known-constant.md) pattern made runnable: a
value that *looked* novel turned out to equal `g^2 / alpha^2`, a combination of two
published constants. A language model in retrieval mode snaps such a value to the
nearest single famous constant and misses the structure; this tool does the
from-scratch arithmetic search and catches it mechanically.

## Requirements

Python 3 (3.6+). **No dependencies** — standard library only. Nothing to install.

## Quick start

From inside this `demo/` folder:

```bash
python novelty_check.py
```

That runs a built-in demonstration on three values and shows what gets caught. You
should see the first value flagged as `g^2 / alpha^2` in under a second.

## Usage

```bash
python novelty_check.py                 # run the built-in demonstration
python novelty_check.py 6.99358445525   # check one value of your own
python novelty_check.py 6.9936 --tol 1e-3
python novelty_check.py --list          # show the known-constant registry
python novelty_check.py --selftest      # confirm the checker works (PASS/FAIL)
```

## Verify it works

```bash
python novelty_check.py --selftest
```

This runs three built-in checks — that the Case 01 value is caught as a `g`/`alpha`
combination, that the constant `g` is caught directly, and that an arbitrary control
value is *not* flagged — and prints `PASS`/`FAIL` for each, then an overall result.
It exits `0` on success.

## What it does *not* do

It does not check arbitrary research, scan documents, or use AI to hunt errors. It
mechanizes one narrow, well-defined check. It would not have caught the truncated
validation set ([Case 02](../case-studies/02-truncated-validation.md)) or the
fabricated statistic ([Case 04](../case-studies/04-fabricated-statistic.md)) — those
took judgment, not code.

And one boundary the tool states in its own output: **a "no collision" result does
NOT prove novelty.** It means nothing in a small registry matched within tolerance.
Absence of a match is not evidence of originality; only judgment decides that. A demo
about not overclaiming does not overclaim about itself.
