# Errors and Violations

This document explains how **errors and violations** are defined, detected,
and reported in `eb-contracts`.

Errors and violations are not incidental implementation details —
they are a core part of how Electric Barometer (EB) enforces correctness,
semantic clarity, and trust at system boundaries.

---

## Why errors and violations are first-class concepts

In many systems, validation failures are treated as nuisances to be worked around.
In EB, they are treated as **signals**.

Errors and violations exist to:

- Surface schema drift early
- Expose semantic ambiguity explicitly
- Prevent silent downstream corruption
- Assign responsibility at the correct boundary

A contract that cannot fail meaningfully is not a contract.

---

## Errors vs violations

`eb-contracts` distinguishes between **violations** and **errors**.

---

### Violations

A *violation* is a detected departure from a contract’s rules.

Examples:
- Missing required columns
- Invalid data types
- Semantic inconsistencies (e.g. horizon mismatch)
- Invalid numeric values

Violations describe *what is wrong*, not how execution should respond.

---

### Errors

An *error* is how the system responds to one or more violations.

Whether a violation becomes an error depends on:

- The active validation mode
- The severity of the violation
- The contract being enforced

This separation allows enforcement behavior to be configurable
without weakening semantics.

---

## Validation modes and behavior

Violations are interpreted differently depending on validation mode:

- **Strict** – violations raise errors immediately
- **Warn** – violations emit warnings but allow continuation
- **Off** – violations are not checked

Validation modes control *response*, not *definition*.
A violation is still a violation even if enforcement is disabled.

---

## Types of violations

Violations generally fall into the following categories.

---

### Schema violations

Schema violations occur when required structure is missing or malformed.

Examples:
- Missing required columns
- Incorrect column data types
- Invalid DataFrame shape

Schema violations indicate structural incompatibility.

---

### Semantic violations

Semantic violations occur when data is structurally valid
but *meaningfully incorrect*.

Examples:
- Horizon values that contradict target dates
- Quantiles outside valid ranges
- Mismatched entity identifiers

Semantic violations are especially dangerous because they often
produce plausible but incorrect results.

---

### Numeric violations

Numeric violations occur when values are not numerically valid.

Examples:
- NaNs where prohibited
- Infinite values
- Negative values where positivity is required

Numeric violations protect downstream mathematical correctness.

---

## Aggregation of violations

Validation may detect **multiple violations** in a single artifact.

EB prefers to:

- Aggregate violations where possible
- Report them together
- Provide clear, actionable messages

This reduces iteration cycles during debugging and onboarding.

---

## Error messaging philosophy

Error and warning messages are designed to be:

- Specific (what failed)
- Localized (where it failed)
- Actionable (how to fix it)
- Deterministic (same input → same message)

Messages are part of the developer experience and are treated accordingly.

---

## Responsibility boundaries

Errors indicate **boundary failures**, not downstream bugs.

If a contract fails validation:

- The producer is responsible for correction
- Consumers should not attempt to compensate
- The artifact should not proceed downstream

This keeps accountability clear and localized.

---

## Common anti-patterns

Avoid:

- Catching and suppressing validation errors silently
- Treating warnings as noise
- Re-validating artifacts deep inside pipelines
- Mutating data to “make it pass” validation

These patterns undermine contract guarantees.

---

## Failure as a design feature

Validation failures are intentional design features.

They:

- Prevent incorrect assumptions from spreading
- Improve long-term system reliability
- Encourage explicit handling of edge cases

A failing contract is safer than a silently corrupted artifact.

---

## Design principles

Errors and violations in EB follow these principles:

- **Fail early**
- **Fail clearly**
- **Fail at boundaries**
- **Separate detection from response**
- **Make meaning explicit**

---

## Summary

Errors and violations are how Electric Barometer speaks when something is wrong.

They are not obstacles to be avoided, but guarantees to be respected.
A contract that fails loudly protects everything downstream.

Treat violations as information.
Treat errors as boundaries.
