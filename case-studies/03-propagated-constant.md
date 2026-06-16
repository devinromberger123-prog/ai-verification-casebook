# Case 03 — A fabricated constant propagated across a body of work

**Domain:** nonlinear dynamics / scaling theory
**Failure mode caught:** a single AI-hallucinated constant that propagated silently into multiple manuscripts
**Disclosure:** generic (described as an exponent-value correction; no project specifics needed)

> This is the most complete demonstration of the discipline in the record. It has all four elements: a fabricated input, silent propagation, a source-audit that found it, and *three independent confirmations* of the correction.

---

## What happened

An exponent value — call it κ = 1.269 — was in use across a body of manuscripts. It was wrong. The correct value is **κ = 1.2265**.

The error did not originate as a typo in κ itself. It traced back one level deeper, to a single **AI-hallucinated underlying constant** early in development. Asked for a reference eigenvalue, a model returned **≈ 7.068** instead of the correct literature value **6.619036513** (Crutchfield, Nauenberg & Rudnick, 1981). Because κ is computed from that eigenvalue,

```
κ = ln(y) / ln(δ)
```

the one bad number produced a wrong κ, and the wrong κ then propagated silently into everything built on top of it. This is the classic LLM numerical failure mode: the formula is right, the structure is right, and one specific constant is confidently wrong.

## Scoping the blast radius

A correction is only half the job; the other half is establishing *what it touched.* Of **ten documents** in the body of work:

- **Four** used κ as a computational input and **required correction.**
- The **other six** were confirmed **unaffected** — they computed a *different* exponent by a *different* route (a circle-map / transfer-operator method) and never used κ as an input at all.

So the audit produced two findings, not one: which documents were wrong, *and* which were provably clean. The second matters as much as the first — it bounds the damage and prevents both under- and over-correction.

## How it was caught and confirmed — three independent ways

The correction was not accepted on the strength of any single model saying so. It was confirmed three ways that do not share a failure mode:

1. **Independent from-scratch convergence.** A completely separate development path arrived at **κ ≈ 1.232** on its own, from scratch — landing on the correct neighborhood without being told the answer.
2. **Direct simulation.** A verification simulation measured **κ_empirical = 1.2260** — **0.0005** away from the correct theoretical value (1.2265), versus **0.0430** away from the wrong value (1.269). That is roughly **86× closer** to correct than to the fabrication.
3. **Collapse-quality test.** A separate bivariate test showed the corrected value produced tighter residuals than the wrong one (**0.583 vs. 0.681**) — independent geometric evidence that 1.2265 is the value the data actually prefers.

Each confirmation reaches the same answer by a different mechanism. That is the point of the discipline: not one strong argument, but several independent ones that would have to fail *together* to be wrong.

## The lesson

A single fabricated constant can propagate silently across an entire body of work, surviving every internal consistency check because everything downstream was built to be consistent *with it.* Catching it requires:

- **auditing back to the primary source** (the 1981 reference), not to a secondary citation or a model's memory of the number;
- **confirming the correction by independent convergence and direct computation**, never by trusting a single model or a majority vote;
- **scoping the blast radius** — establishing both what the error corrupted and what is provably clean.

A note on framing: the underlying value being grounded in literature makes the corrected work *stronger*, not weaker. κ = 1.2265 is anchored to an established 1981 result; κ = 1.269 would have required defending an unexplained deviation from it. The correction is a refinement that strengthens the foundation.
