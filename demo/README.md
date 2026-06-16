# Demo — known-constant checker (planned)

This folder is intentionally a placeholder. The repository ships **lean and finished** as a casebook plus protocol; this demo is the single planned addition, scoped narrowly and honestly.

## What it will do

A small, self-contained script that mechanizes the *one* check from the protocol that genuinely automates (protocol step 4):

> Given a quantity and its definition, recompute it from scratch, and flag it when it collides with a known published constant.

The intended experience: a stranger clones the repo, runs one command, and watches it catch a planted "is this 'new' value actually a known constant?" error — the [Case 01](../case-studies/01-known-constant.md) pattern — in under ninety seconds.

## What it will *not* do

It will not check arbitrary research, scan documents, or use AI to hunt errors. It mechanizes one narrow, well-defined check. It would not have caught the truncated validation set ([Case 02](../case-studies/02-truncated-validation.md)) or the fabricated statistic ([Case 04](../case-studies/04-fabricated-statistic.md)) — those took judgment, not code. The demo is a demonstration of the one automatable piece, not a tool that replaces the discipline.

## Why it's separated out

Shipping the casebook finished matters more than shipping it feature-complete. The demo is a clean add that requires no changes to anything already here. If you are reading this in the published repo and the folder is still a placeholder, the casebook and protocol stand on their own — the demo is gravy, not foundation.
