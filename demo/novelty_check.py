#!/usr/bin/env python3
"""
novelty_check.py - Known-constant collision checker

A small, runnable demonstration of the ONE check from the AI Verification Casebook
that genuinely automates. See ../PROTOCOL.md (step 4) and
../case-studies/01-known-constant.md.

THE CASE 01 PATTERN, MECHANIZED
-------------------------------
In Case 01, a value computed from a definition *looked* possibly novel - but it was
actually a re-expression of published constants (it equaled g^2 / alpha^2, to the
precision g is known to). A language model in retrieval/lookup mode, handed that
value, snaps to the nearest famous constant and reports *that*. This tool instead
does the from-scratch arithmetic search: it computes known constants and their simple
combinations and reports, mechanically, whether your "new" value is in fact one of
them.

SCOPE - READ THIS
-----------------
This mechanizes ONE narrow check. A reported collision is strong evidence your value
is NOT new. The ABSENCE of a collision does NOT prove novelty - it only means nothing
in this small registry matched within tolerance. Judgment, not this script, decides
novelty. Stating that boundary plainly is the whole point of the casebook: a tool
about not overclaiming must not overclaim about itself.

Pure Python standard library. No dependencies.

USAGE
-----
    python novelty_check.py                 # run the built-in demonstration
    python novelty_check.py 6.99358445525   # check one value of your own
    python novelty_check.py 6.9936 --tol 1e-3
    python novelty_check.py --list          # show the known-constant registry
    python novelty_check.py --selftest      # confirm the checker works (PASS/FAIL)
"""

import argparse
import math
import sys

# --------------------------------------------------------------------------- #
# The registry of known, published constants.
# Domain constants (the ones relevant to the Case 01 story) plus universal ones,
# so the tool is generally useful and not a one-trick prop.
# --------------------------------------------------------------------------- #
KNOWN_CONSTANTS = {
    # name        value                  short description / source
    "delta":   (4.669201609102990, "Feigenbaum delta (period-doubling rate)"),
    "alpha":   (2.502907875095892, "Feigenbaum alpha (spatial scaling constant)"),
    "g":       (6.619036513,       "Crutchfield-Nauenberg-Rudnick additive-noise eigenvalue (1981)"),
    "pi":      (math.pi,           "pi"),
    "e":       (math.e,            "Euler's number"),
    "phi":     ((1.0 + 5.0 ** 0.5) / 2.0, "golden ratio"),
    "sqrt2":   (2.0 ** 0.5,        "square root of 2"),
    "gamma":   (0.5772156649015329, "Euler-Mascheroni constant"),
    "catalan": (0.9159655941772190, "Catalan's constant"),
}

# A value chosen to have no clean re-expression in the registry (used by --selftest).
NOVEL_CONTROL = 8.5391274


def _rel_err(a, b):
    """Relative error between a and b (falls back to absolute if b == 0)."""
    if b == 0.0:
        return abs(a - b)
    return abs(a - b) / abs(b)


def _fmt_power(name, p):
    """Readable form of name**p for p != 1, e.g. g^2, 1/alpha, alpha^-3."""
    if p == 1:
        return name
    if p == -1:
        return "1/" + name
    return "{}^{}".format(name, p)


def _fmt_combo(a_name, e1, b_name, e2):
    """Readable form of (a**e1)*(b**e2) where e2 < 0, e.g. 'g^2 / alpha^2'."""
    num = a_name if e1 == 1 else "{}^{}".format(a_name, e1)
    den_p = -e2
    den = b_name if den_p == 1 else "{}^{}".format(b_name, den_p)
    return "{} / {}".format(num, den)


def find_collisions(value, rel_tol=1e-4):
    """
    Search the registry for known constants - and simple combinations of them -
    that match `value` within `rel_tol`. Returns a list of
    (expression, computed_value, relative_error), de-duplicated by value and
    sorted closest first.
    """
    names = list(KNOWN_CONSTANTS)
    raw = []  # (expr, value, err)

    # 1) direct matches against each constant
    for n in names:
        v = KNOWN_CONSTANTS[n][0]
        err = _rel_err(value, v)
        if err <= rel_tol:
            raw.append((n, v, err))

    # 2) single-constant powers (skip 1; that is the direct case above)
    for n in names:
        base = KNOWN_CONSTANTS[n][0]
        for p in (-3, -2, -1, 2, 3):
            v = base ** p
            err = _rel_err(value, v)
            if err <= rel_tol:
                raw.append((_fmt_power(n, p), v, err))

    # 3) two-constant combinations: a^e1 * b^e2, with e2 negative (a denominator)
    for i in range(len(names)):
        for j in range(len(names)):
            if i == j:
                continue
            a = KNOWN_CONSTANTS[names[i]][0]
            b = KNOWN_CONSTANTS[names[j]][0]
            for e1 in (1, 2):
                for e2 in (-1, -2):
                    v = (a ** e1) * (b ** e2)
                    err = _rel_err(value, v)
                    if err <= rel_tol:
                        raw.append((_fmt_combo(names[i], e1, names[j], e2), v, err))

    # de-duplicate by computed value (keep the shortest expression), then sort
    best = {}
    for expr, v, err in raw:
        key = round(v, 9)
        if key not in best or len(expr) < len(best[key][0]):
            best[key] = (expr, v, err)
    out = sorted(best.values(), key=lambda t: t[2])
    return out


def check_value(value, rel_tol):
    """Check one value and print a verdict. Returns True if a collision was found."""
    print()
    print("  Checking value: {!r}   (relative tolerance: {:g})".format(value, rel_tol))
    hits = find_collisions(value, rel_tol)
    if hits:
        print("  >> COLLISION FOUND - this value is a re-expression of known constant(s):")
        for expr, v, err in hits:
            print("       {:.11g}  =  {}  =  {:.11g}    (rel. error {:.1e})".format(
                value, expr, v, err))
        print("  >> Treat as NOT NOVEL. It matches published quantities; verify the")
        print("     primary source before claiming it as new.")
        return True
    else:
        print("  >> No collision found in the registry within tolerance.")
        print("  >> This does NOT prove novelty. It means nothing in this small registry")
        print("     matched. Widen the registry, then apply judgment - the script cannot.")
        return False


def list_registry():
    print()
    print("  Known-constant registry ({} constants):".format(len(KNOWN_CONSTANTS)))
    print("  " + "-" * 64)
    for name, (value, desc) in KNOWN_CONSTANTS.items():
        print("    {:8s} = {:<20.15g}  {}".format(name, value, desc))
    print()
    print("  The checker also searches simple combinations of these: powers up to")
    print("  +/-3, and ratios a^e1 / b^e2. That is how it catches a value like")
    print("  g^2 / alpha^2, which is not a constant itself but a combination of two.")
    print()


def run_demo(rel_tol):
    print("=" * 72)
    print("  AI VERIFICATION CASEBOOK - known-constant collision checker (demo)")
    print("=" * 72)
    print("  Mechanizing the Case 01 check: is a 'new' value actually a known one?")
    print("  Three values are checked below. Watch what gets caught.")

    planted = [
        ("6.99358445525", 6.99358445525,
         "A variance ratio reached by an independent computation. It LOOKED novel."),
        ("6.619036513", 6.619036513,
         "A value that is simply the published constant g itself."),
        ("{}".format(NOVEL_CONTROL), NOVEL_CONTROL,
         "An arbitrary value with no clean re-expression in the registry."),
    ]

    for label, value, note in planted:
        print()
        print("-" * 72)
        print("  {}".format(note))
        check_value(value, rel_tol)

    print()
    print("=" * 72)
    print("  Takeaway: the first value was NOT new - it is g^2 / alpha^2, a")
    print("  re-expression of two published constants, caught mechanically. A")
    print("  retrieval-mode model would have snapped it to the nearest single")
    print("  constant (g) and missed the structure. The third value is not flagged -")
    print("  but that is NOT proof it is novel. Only judgment decides that.")
    print("=" * 72)
    print()
    print("  Try your own:   python novelty_check.py <value>")
    print("  See the list:   python novelty_check.py --list")
    print("  Verify it works: python novelty_check.py --selftest")
    print()


def selftest():
    print()
    print("  Running self-test...")
    print("  " + "-" * 64)
    ok = True

    # 1) The Case 01 value must be flagged as a g / alpha combination.
    hits1 = find_collisions(6.99358445525, 1e-4)
    exprs1 = [h[0] for h in hits1]
    case01 = any(("g" in x and "alpha" in x) for x in exprs1)
    print("  [{}] Case 01 value (6.99358445525) flagged as a g/alpha combination".format(
        "PASS" if case01 else "FAIL"))
    ok = ok and case01

    # 2) The constant g must be flagged as a direct match.
    hits2 = find_collisions(6.619036513, 1e-7)
    direct_g = "g" in [h[0] for h in hits2]
    print("  [{}] g (6.619036513) flagged as a direct known constant".format(
        "PASS" if direct_g else "FAIL"))
    ok = ok and direct_g

    # 3) An arbitrary control value must NOT be flagged.
    hits3 = find_collisions(NOVEL_CONTROL, 1e-4)
    clean = (len(hits3) == 0)
    print("  [{}] arbitrary control value ({}) correctly NOT flagged".format(
        "PASS" if clean else "FAIL", NOVEL_CONTROL))
    ok = ok and clean

    print("  " + "-" * 64)
    print("  SELF-TEST: {}".format(
        "ALL PASS - the checker works as intended." if ok
        else "FAILURE - see the failing line(s) above."))
    print()
    return ok


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        description="Known-constant collision checker (AI Verification Casebook demo).")
    parser.add_argument("value", nargs="?", type=float,
                        help="a numeric value to check (omit to run the built-in demo)")
    parser.add_argument("--tol", type=float, default=1e-4,
                        help="relative tolerance for a match (default: 1e-4)")
    parser.add_argument("--list", action="store_true",
                        help="print the known-constant registry and exit")
    parser.add_argument("--selftest", action="store_true",
                        help="run built-in checks and report PASS/FAIL")
    args = parser.parse_args(argv)

    if args.list:
        list_registry()
        return 0
    if args.selftest:
        return 0 if selftest() else 1
    if args.value is not None:
        check_value(args.value, args.tol)
        return 0
    run_demo(args.tol)
    return 0


if __name__ == "__main__":
    sys.exit(main())
