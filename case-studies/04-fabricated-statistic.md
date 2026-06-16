# Case 04 — A fabricated statistic in another field

**Domain:** institutional / market research (non-mathematical)
**Failure mode caught:** unsourced and outdated figures used as load-bearing inputs
**Disclosure:** anonymized (no institution or client named)

> Included because it shows the discipline is **domain-general.** The same habit that catches a hallucinated physics constant catches a fabricated retention statistic — the field changes, the move doesn't.

---

## What happened

In a research task with no mathematics in it at all, an AI produced two flawed figures, and downstream analysis was built on both before they were checked.

**Failure one — an outdated, mis-applied baseline.** A retention rate of **~52%** was used as the baseline for a set of financial projections. That number was not invented out of nothing, but it was wrong for the purpose: it was an **average of three superseded annual rates** from an earlier period, presented as if it were the current figure. The actual current, sourced rate was **64.9%** — materially different, and high enough that it inverted the entire value proposition (from "fix poor retention" to "optimize already-strong retention"). Every projection built on the 52% baseline was invalidated.

**Failure two — a genuinely fabricated correlation.** Separately, a claim was asserted that career clarity produces **"40–70% better retention"** — a specific, confident, load-bearing statistic with no study behind it. A literature search turned up **nothing supporting it.** It was not outdated or mis-applied; it simply did not exist. The honest finding was that the real effect is modest and could not be quantified the way the claim implied.

## How it was caught

The same way as the quantitative cases: by **checking each load-bearing number against a current primary source**, and by **refusing to let an unsourced correlation stand** just because it sounded plausible and supported the desired conclusion. A figure that "sounds about right" and happens to strengthen your pitch is exactly the figure to distrust first.

## The lesson

The discipline does not depend on the subject being mathematics. Wherever a number is doing real work in an argument:

- **verify it against a current, primary source** — not a secondary citation, not a model's recollection, not last cycle's figure presented as this cycle's;
- treat **"a number that sounds right" as a hypothesis, not a source** — especially when the number happens to support the conclusion you want;
- when a statistic is load-bearing and you cannot source it, **say so**, and rebuild the argument on what you *can* source.

The cross-domain reach is itself part of the point: this is a way of working, not a trick that only applies to constants.
