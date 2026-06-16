# The Protocol

A checklist for catching confident-but-wrong AI output in quantitative and sourced work. This is the generalized form of the discipline the [case studies](case-studies/) demonstrate.

**What this is:** a discipline you apply *by hand*, with AI as a bounded instrument. It is not software. It does not run itself. The judgment it encodes — knowing which claim to distrust — is the part that matters and the part that cannot be automated.

**Where it applies:** any field where numbers or sourced claims do real work — empirical research, finance, data science, institutional analysis. The principles are domain-general (Case 04 shows the same discipline crossing from mathematics into institutional research). One narrow piece — recomputing a stated quantity and flagging collisions with known values — can be mechanized; the rest is human judgment by design.

---

## Setup: separate the roles

Before any checking happens, structure the work so that errors have an independent chance of being caught.

- **Never let the same system draft and check.** The system that produces a number must not be the system that verifies it. An error introduced in one role is then exposed to a fresh look in another.
- **Use independent reviewers.** Have models attack a draft from outside, not just refine it from inside.
- **Keep a human adjudicator.** Disagreements are resolved by a person doing the deciding check — not by the models voting among themselves.

---

## The two governing rules

These are the load-bearing principles. Everything else is application.

1. **Resolve disagreements by direct computation — never by majority vote among models.** Three models agreeing can be three models sharing one mistake; agreement among correlated systems launders error rather than removing it. When models disagree, the tiebreaker is a computation you can inspect, not a head count.

2. **Reproduce blind.** When you ask for a quantity to be reproduced, hand over the **definitions only** — never the target answer. A reproduction that has seen the answer cannot be trusted to have found it independently. Blind reproduction is the difference between confirmation and contamination.

---

## The checklist

Run these against any result before you rely on it or publish it.

1. **List the load-bearing numbers and claims.** Which values, if wrong, would change the conclusion? Those are the ones to audit. Don't spread attention evenly; spend it where the result is structurally exposed.

2. **Audit each to its primary source.** Not a secondary citation, not a model's memory of the number, not last cycle's figure presented as this cycle's. Go to the original. (Cases 03 and 04.)

3. **Reproduce computed quantities blind.** For anything computed, reproduce it independently from the definitions, without handing over the target. (Case 01.)

4. **When a value sits near a famous constant, force a from-scratch recompute.** Retrieval-mode tools snap to the nearest known value when your candidate is close to one. If the model is not visibly executing code, assume it has substituted the neighbor. Make it compute, and confirm computation ran. (Case 01.)

5. **Reverse-audit symptoms to their source.** When a downstream number looks off, back-calculate what input would have produced it and compare that reconstructed input to what you believe the input was. The gap is the bug. (Case 02.)

6. **When a fix makes the numbers "work," check whether it makes the result *correct*.** Consistency is not validity. The patch that silences a discrepancy can bury the very finding the discrepancy was pointing at. (Case 02.)

7. **Scope the blast radius.** When you find one error, establish *both* what it corrupted *and* what is provably clean. A correction without a scope is half-done, and risks both under- and over-correcting. (Case 03.)

8. **Verify identity, not just existence.** Two sources with near-identical names and different contents will pass a spelling check and an "exists?" check. Confirm the *correct* source by content, against the source of record — especially before anything locks (preregistration, publication, frozen release). (Case 05.)

9. **Confirm corrections by independent means.** Don't accept a correction on one model's say-so. Seek confirmation by mechanisms that don't share a failure mode — independent from-scratch convergence, direct simulation, a separate quality test. Several independent confirmations that would have to fail *together* beat one confident assertion. (Case 03.)

---

## The mode-not-model rule

State this one explicitly, because it is widely useful and widely missed.

The **same model** can compute or retrieve. For a discovery or computation step, reliability depends on **which mode it is in**, not which model it is. A model executing code recovers the real quantity; the same model in retrieval / lookup mode, faced with a value near a known constant, returns the known constant. The brand is not the variable. *Whether it computed or retrieved* is the variable — and the verification is the tell: an answer only counts if you can see the computation ran.

---

## What this catches — and what it doesn't

Stated plainly, because a protocol about not overclaiming should not overclaim:

- **The judgment generalizes, but does not automate.** Knowing which claim to distrust, smelling that a value near a famous constant needs a recompute, sensing that a fix is papering over something — these transfer across fields but cannot be reduced to a script. This is the skill. It is demonstrated, not packaged.
- **One check mechanizes.** "Is this stated quantity actually a known constant, and does it recompute from its definition?" genuinely automates — see [`demo/`](demo/). But it catches one class of error. It would not have caught the truncated validation set or the fabricated statistic. Those took judgment, not code.

Use the protocol as a discipline. Use the demo as a demonstration of the one piece that runs on its own. Don't mistake either for the other.
