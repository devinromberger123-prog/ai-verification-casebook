# Case 01 — A "new" constant was already known

**Domain:** nonlinear dynamics / renormalization scaling
**Failure mode caught:** a possibly-novel quantity that was actually a re-expression of a published one
**Disclosure:** full (this result is going public independently)

---

## The claim under test

A variance-accumulation ratio — call it Λ(2) = 6.99358445525 — had been reached by an independent orbit-recurrence computation (propagating a concrete variance recurrence rather than constructing the usual abstract renormalization operators). Because it arrived by an unusual route and didn't obviously match anything, it looked like it *might* be a new constant.

The question put to the verification process was deliberately narrow: **is this value already known, expressed differently?**

## What the method found

It is. The quantity factors cleanly as

```
Λ(2) = ρ₂ / α²  =  g² / α²
```

where:

- **ρ₂ ≈ 43.81164** is the p = 2 spectral radius already tabulated in Díaz-Espinosa & de la Llave (2007), Table 1;
- **g ≈ 6.619** is the period-doubling additive-noise scaling eigenvalue (Crutchfield, Nauenberg & Rudnick, 1981), and ρ₂ ≈ g² ≈ 43.81 (the two agree to the precision g is known to);
- **α** is the Feigenbaum spatial constant.

Λ(2) is therefore a re-expression of a published quantity — obtainable by dividing two numbers already printed in a 2007 table. The agreement holds to about **six significant figures**, which is the precision to which g is independently known. It is not a new constant.

> **An honest distinction the repo keeps.** Reaching a known endpoint by an independent computational route demonstrates that the route *works* — and that is genuinely useful, because the same back-road method might generalize to problems where no published endpoint exists. But arriving at a known value is not a discovery, and the writeup says so plainly. An early draft of this result overstated the agreement as "nine significant figures, the full precision of g"; the verification process corrected it to six, because the independent literature only pins g to six. Catching your own overstatement is part of the discipline.

## The kicker: retrieval vs. computation

While confirming the value, a second, more broadly useful thing surfaced.

Several models were handed the **definitions only** — never the target — and asked to reproduce the quantity blind. The split was clean and reproducible:

- Models that **executed code** computed **6.9936**.
- Models operating in **retrieval / lookup mode** (in this instance Gemini and DeepSeek) returned the nearest *published* constants instead: **g² ≈ 43.81** and **g ≈ 6.619**.

The retrieval-mode runs received the same prompt as the code-execution runs. Their convergence on the nearest famous constant was observed behavior, not an induced or adversarial result.

This did two things at once:

1. It **demonstrated the failure mode** — a value sitting numerically adjacent to a well-known constant pulls retrieval-biased responses toward that constant.
2. It was **itself evidence** that 6.9936 was not a tabulated constant: if it had been, a lookup would have found *it*, not its famous neighbor.

## The lesson

AI assistance is reliable for a discovery or computation step **only when the model actually executes the computation.** In retrieval mode, when your candidate value is near a known one, the model will quietly substitute the known one and hand it to you with confidence. This generalizes well beyond this problem — see the discussion in the main README, and the protocol step on forcing computation.
