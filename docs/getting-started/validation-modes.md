# Validation Modes

This guide explains **validation modes** in `eb-contracts` and how they control
the behavior of contract enforcement across different Electric Barometer (EB)
environments.

Validation modes allow the *same contracts* to be used consistently in
research, CI, and production — without duplicating logic or weakening guarantees.

---

## Why validation modes exist

Electric Barometer contracts are designed to be **strict by default**,
but real-world workflows vary:

- Research notebooks favor iteration speed
- CI pipelines require hard guarantees
- Production ingestion must fail fast and loudly
- Legacy pipelines may require gradual adoption

Validation modes make enforcement **configurable but explicit**.

---

## The three validation modes

`eb-contracts` supports three validation modes:

- `strict`
- `warn`
- `off`

Each mode controls how violations are handled at validation time.

---

## Strict mode

**Strict mode** treats all contract violations as errors.

Behavior:
- Validation failures raise exceptions
- Artifact construction is aborted
- Downstream execution cannot proceed

Use strict mode when:
- Running CI or automated tests
- Ingesting production data
- Producing artifacts consumed by others

Strict mode is the **default and recommended baseline**.

---

## Warn mode

**Warn mode** allows validation to proceed while emitting warnings.

Behavior:
- Violations are reported as warnings
- Artifact construction succeeds
- Execution continues

Use warn mode when:
- Exploring data interactively
- Debugging schema mismatches
- Gradually adopting contracts in legacy systems

Warn mode is transitional — not a long-term substitute for strict enforcement.

---

## Off mode

**Off mode** disables validation entirely.

Behavior:
- No validation checks are executed
- Artifacts are constructed without guarantees
- Violations are not detected

Use off mode only when:
- Artifacts are already guaranteed valid
- Performance constraints are extreme
- Validation is handled externally

Off mode should be rare and intentional.

---

## Setting the validation mode

Validation mode is set programmatically:

```python
from eb_contracts.validate import set_validation_mode

set_validation_mode("strict")
```

The mode applies globally for the current process.

---

## Mode selection guidelines

Recommended defaults:

- **CI pipelines** → `strict`
- **Production ingestion** → `strict`
- **Research notebooks** → `warn`
- **Trusted internal pipelines** → `strict` or `off` (with caution)

When in doubt, choose strict.

---

## What validation covers (and what it doesn’t)

Validation modes control *how violations are handled*, not *what is validated*.

Validation always checks:
- Schema correctness
- Required fields
- Semantic consistency
- Numeric validity

Modes only change the **response**, not the **rules**.

---

## Validation is not optional governance

Even in warn or off mode, contracts still define:

- Canonical schemas
- Semantic meaning
- Version boundaries

Disabling validation does not change what the contract *means* —
only whether enforcement is active.

---

## Common anti-patterns

Avoid:

- Leaving validation off permanently
- Switching modes implicitly based on environment variables
- Catching and suppressing validation errors silently

Validation mode changes should be **explicit and intentional**.

---

## Failure philosophy

Validation failures are signals, not inconveniences.

A failure indicates:
- Schema drift
- Semantic ambiguity
- Unsafe assumptions

Fixing validation failures improves system reliability downstream.

---

## Design principles

Validation modes follow these principles:

- **Same contracts everywhere**
- **Configurable enforcement**
- **Explicit failure behavior**
- **No silent weakening of semantics**

---

## Summary

Validation modes let Electric Barometer scale across environments
without compromising semantic integrity.

Use strict mode by default.
Use warn mode to transition.
Use off mode rarely — and knowingly.

Validation is the contract’s voice. Let it speak.
