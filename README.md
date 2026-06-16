# AI Verification Casebook

A documented discipline for catching confident-but-wrong AI output in quantitative and sourced work — with five worked cases where it caught real errors before they shipped.

The marketable skill on display here is narrow and specific: **catching the confident, plausible, wrong outputs that quietly kill a result** — by auditing claims back to their source and resolving disagreements through direct computation rather than trusting model output or majority vote. Every case below is a real error caught in the author's own research, documented honestly, with the proprietary specifics removed.

---

## What this is — and what it isn't

**It is** a casebook plus a protocol. The case studies (`case-studies/`) are worked examples of a verification discipline catching real errors. The protocol (`PROTOCOL.md`) generalizes that discipline into a checklist you can apply by hand to your own AI-assisted work.

**It is not** a hosted tool, a service, or software that scans your documents. Nothing here phones home, watches your work, or uses AI to hunt errors in arbitrary input. The discipline is human-applied, with AI used as a bounded instrument. An optional runnable demo of the *one* check that genuinely automates is planned (`demo/`); everything else is judgment, and judgment doesn't ship as a binary.

This honesty is deliberate. A repository about not overclaiming should not overclaim about itself.

---

## The thesis

Most "AI made a mistake" stories are typos. These aren't. In each case an AI produced a result that was internally coherent, confidently stated, and wrong — and in several, it had already propagated into downstream work before it was caught. What caught it was not a better model. It was a discipline:

1. **Resolve disagreements by direct computation, never by majority vote among models.** Majority vote launders correlated error; independent computation doesn't. Three models agreeing can be three models making the same mistake.
2. **Reproduce blind.** A reproduction is handed the *definitions only*, never the target answer — so it cannot be contaminated by the value it is supposed to find.
3. **Never let the same system draft and check.** An error introduced in one role then has an independent chance of being caught in another.

These are not exotic. The contribution is not the principles; it is having applied them with discipline and documented what they caught.

---

## The workflow

The author runs an adjudicator-directed, role-separated, multi-model workflow. The human is the adjudicator; the AI systems are bounded tools assigned to roles that don't overlap.

| Role | System(s) | Job |
|---|---|---|
| Architecture + adversarial review | Claude | structural decisions; hostile audit of claims |
| Long-form drafting | GPT-5 | produces prose / LaTeX / code drafts |
| Independent hostile reviewers | Gemini, Grok | attack the draft from outside |
| Citation check + code-execution reproduction | Perplexity | verifies sources; recomputes constants |
| **Adjudicator + final numerical verification** | **Human** | resolves disagreements; final check on own machine |

The point of the separation is mechanical, not ceremonial: the system that drafts a number is never the system that checks it, and the system that checks it is never told the answer in advance.

---

## A generalizable finding: it's the *mode*, not the *model*

One case surfaced a failure mode worth stating on its own, because it can save other researchers real time.

When a freshly computed quantity lands numerically near a famous published constant, language models operating in **retrieval / lookup mode are systematically biased toward the published value** — they pattern-match to the known constant and return *that* — whereas the same model family, **executing code**, recovers the actual computed quantity.

This was observed directly. Handed an identical definitions-only prompt, code-execution runs computed the real value (~6.9936); retrieval-mode runs instead returned the nearest tabulated constants (≈43.81 and ≈6.619). The value sat in the "danger zone" right next to a well-known eigenvalue, which is exactly what a retrieval-biased response reaches for.

The conclusion is **not** "AI can't produce novel results." It is sharper and more useful: *the same model can compute or retrieve, and for a discovery or computation step it is reliable only when it is visibly executing the computation.* If you are using AI to find or verify a quantity that might be new, and it is not running code, assume it has substituted the nearest known answer. Force computation, and verify that computation ran.

---

## The cases

Each is a short, self-contained case study. Start with **03** — it is the most complete demonstration of the discipline in the record.

| # | Case | Domain | What it shows |
|---|---|---|---|
| [01](case-studies/01-known-constant.md) | A "new" constant was already known | Nonlinear dynamics | A possibly-novel value resolved to a re-expression of a published one — and the retrieval-vs-computation contrast above. |
| [02](case-studies/02-truncated-validation.md) | Silent validation on ~2% of the data | Signal processing | A buried truncation caught by reverse-auditing a symptom to its source — which then exposed a real property of the method. |
| [03](case-studies/03-propagated-constant.md) | **A fabricated constant propagated across a body of work** | Nonlinear dynamics | One AI-hallucinated number propagated into four documents; caught by source-auditing and confirmed three independent ways. **The flagship case.** |
| [04](case-studies/04-fabricated-statistic.md) | A fabricated statistic in another field | Institutional research | The discipline is domain-general: load-bearing numbers verified against current primary sources. |
| [05](case-studies/05-database-identity.md) | An identifier collision caught before lock | Research data | Two near-identically named public databases; caught and corrected in a preregistration. |

---

## How to use this

- **Read it** as evidence of judgment — this is the primary purpose.
- **Apply the protocol** (`PROTOCOL.md`) to your own AI-assisted quantitative or sourced work.
- **Run the demo** (`demo/`, when available) to see the one automatable check in action.

The discipline's *principles* generalize across any quantitative or sourced field — finance, data science, empirical research, institutional analysis. Case 04 already shows it crossing from mathematics into institutional research. The *automatable* portion generalizes only to its own narrow problem class (recomputing a stated quantity and flagging collisions with known values); the rest is human judgment by design. Both boundaries are stated plainly throughout, on purpose.

---

## Scope and omissions

Some cases arose in research with intellectual property at stake. Those are described in **methodology terms only** — the verification point is preserved; the proprietary mechanism, feature definitions, and domain-specific specifics are not present. One case involved a third party and is anonymized. Where a detail is not needed to make the verification point, it has been cut. This is a constraint on disclosure, not on accuracy: every number and event below is real.

---

**Author:** Devin Romberger — Old Faithful Consulting LLC
**License:** [MIT](LICENSE)
