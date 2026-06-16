# Case 05 — An identifier collision caught and corrected in a preregistration

**Domain:** research data / preregistration
**Failure mode caught:** two near-identically named public datasets, one nearly used in place of the other
**Disclosure:** generic (no project specifics)

> A small, clean example of a distinct failure class: not a wrong *value*, but a wrong *identity* — the right operation applied to the wrong source.

---

## What happened

A study drew on public physiological databases. Two of those databases had **near-identical identifiers**, differing by roughly a single character, but contained **entirely different data.** The wrong one was referenced, and the error made it into a **preregistration draft** — a document whose whole purpose is to be locked before analysis.

## How it was caught

The error entered a preregistration draft and was caught on audit, with a correction requested from the registry. The two identifiers were checked against the **source of record** — confirming not just that *a* database with that name existed, but that it was the *specific* database holding the data actually used. The mismatch was caught, the reference corrected, and the registry notified so the preregistration could be amended.

Identifier collisions are insidious precisely because both names resolve to something real. A spelling check passes. A "does this source exist" check passes. Only a "is this the *correct* source, by content" check catches it.

## The lesson

- **Verify identity, not just existence.** Two sources with near-identical names and different contents is a classic silent-error pattern. Confirm against the source of record by *content*, not by name.
- **Check before anything locks.** Preregistrations, published methods sections, and frozen releases are the worst places for an identity error to survive, because their value depends on being fixed. Audit identifiers *before* the lock, not after.
