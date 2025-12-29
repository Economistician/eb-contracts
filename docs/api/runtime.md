# Runtime API

This document describes the **runtime control surface** exposed by `eb-contracts`.

The Runtime API governs **how contracts are enforced at execution time**,
without changing what contracts mean. It controls validation behavior,
not contract semantics.

---

## Scope of this API

This API covers:

- Global validation mode configuration
- Runtime behavior of contract enforcement
- Guarantees and limitations of runtime controls

It does *not* cover:

- Contract definitions
- Schema or semantic rules
- Migration logic
- Artifact construction APIs

Runtime controls affect **enforcement**, not **meaning**.

---

## Why a runtime API exists

Electric Barometer (EB) contracts are used across environments with different needs:

- Continuous integration pipelines
- Production ingestion systems
- Research and exploratory notebooks
- Legacy systems under migration

A single enforcement policy does not fit all environments.

The Runtime API allows **explicit, centralized control** over how validation
responds to violations — without weakening the contracts themselves.

---

## Core principle

> **Runtime configuration may change enforcement behavior,
> but it must never change contract semantics.**

A contract means the same thing regardless of runtime settings.

---

## Global runtime behavior

Runtime configuration is **process-wide**.

Once set, validation behavior applies to all contract validations
performed in the current Python process.

This ensures consistency and prevents partial enforcement.

---

## Validation modes

The runtime supports three validation modes:

- `strict`
- `warn`
- `off`

These modes control how detected violations are handled.

---

## `set_validation_mode`

```python
set_validation_mode(mode: str) -> None
```

Sets the global validation mode.

---

## Parameters

### `mode` (required)

The validation mode to apply.

Allowed values:
- `"strict"`
- `"warn"`
- `"off"`

Invalid values raise an error immediately.

---

## Mode semantics

---

### Strict mode

Behavior:
- All violations raise exceptions
- Artifact construction is aborted
- Downstream execution cannot proceed

Use strict mode for:
- CI pipelines
- Production ingestion
- Shared artifacts consumed by others

Strict mode is the default and recommended baseline.

---

### Warn mode

Behavior:
- Violations emit warnings
- Artifact construction succeeds
- Execution continues

Use warn mode for:
- Exploratory analysis
- Debugging schema mismatches
- Gradual contract adoption

Warn mode is transitional, not a permanent solution.

---

### Off mode

Behavior:
- Validation is bypassed
- No violations are detected
- No enforcement guarantees exist

Use off mode only when:
- Artifacts are already guaranteed valid
- Validation is handled externally
- Performance constraints are extreme

Off mode must be used deliberately and sparingly.

---

## What runtime does NOT control

The runtime API does *not*:

- Change required columns
- Relax semantic rules
- Alter unit definitions
- Modify versioning guarantees

Runtime configuration never redefines correctness.

---

## Error and warning behavior

- Errors raised in strict mode are deterministic
- Warnings emitted in warn mode are explicit and actionable
- Off mode produces no signals

Consumers must not suppress or ignore runtime signals silently.

---

## Interaction with libraries and frameworks

Because runtime behavior is process-wide:

- Set validation mode early in application startup
- Avoid changing modes dynamically mid-pipeline
- Treat mode changes as configuration decisions

Library code should not override runtime settings implicitly.

---

## Anti-patterns

Avoid:

- Switching validation modes implicitly based on environment variables
- Toggling modes inside library code
- Leaving validation permanently disabled
- Catching and suppressing validation errors silently

These patterns undermine contract guarantees.

---

## Design principles

The Runtime API follows these principles:

- **Explicit configuration**
- **Process-wide consistency**
- **No semantic weakening**
- **Fail-fast defaults**
- **Clear enforcement signals**

---

## Summary

The Runtime API controls *how strictly* Electric Barometer contracts are enforced,
not *what they mean*.

By separating enforcement from semantics,
EB enables consistent contracts across environments
while preserving correctness and trust.

Configure deliberately.
Validate consistently.
