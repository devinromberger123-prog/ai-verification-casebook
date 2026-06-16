# Case 02 — Silent validation on ~2% of the data

**Domain:** signal processing (physiological time series)
**Failure mode caught:** a buried truncation that silently shrank the validation set — and masked a real artifact
**Disclosure:** methodology only (this arose in patent-pending work; no proprietary detail is present)

---

## What happened

A signal-processing pipeline was, unknowingly, validating on only the **first ~2,000 samples** of each recording — out of **80,000+ samples** per subject. That is roughly **2% of each record.** The truncation lived in the extraction script, upstream of everything else, and propagated silently: every downstream result was computed on the short segment without anyone choosing that on purpose.

## How it was caught

By **reverse-auditing from the symptom back to the source.**

A downstream metric implied a certain number of analysis windows per subject. The implied counts came out to roughly **7–35 windows** — which back-calculates to about **800–3,000 samples** per subject, not the tens of thousands a full recording contains. That mismatch, between the data size the results *implied* and the data size the recordings actually *held*, was the entire tell. Nothing in the output said "truncated." The number of windows did.

The general move: when a downstream quantity looks off, back-calculate what input would have produced it, and compare that reconstructed input to what you believe the input actually was. The gap is the bug.

## The deeper finding — why this one matters

The easy fix was obvious and wrong: truncate *everyone* to 2,000 samples so the new data matched the old. That would have made the numbers consistent.

Instead the question asked was: **"but is the result even valid then? That's a few percent of the data — how can we call it definitive?"**

That question exposed a genuine methodological boundary. The metric **saturates on long records.** As the sample size grows, within-bin variance collapses, and the relevant exponent pins monotonically to a ceiling — so the full-length computation doesn't just differ from the short one, it degenerates. The short-segment values weren't an accident to be normalized away; they were the regime in which the metric carried information at all.

So the audit did two things. It caught a silent slip *and* it revealed a real property of the method — one that has direct consequences for how the metric must be applied and reported.

## The lesson

Two, actually:

1. **Reverse-audit symptoms to source.** A wrong downstream number is a pointer to an upstream cause; back-calculate to find it.
2. **When a fix makes the numbers "work," ask whether it makes the result *correct*.** Consistency is not validity. The fix that silences a discrepancy can also bury the finding the discrepancy was pointing at.
