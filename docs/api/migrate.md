# Migration API

This document describes the **public API surface** for migration utilities
exposed by `eb-contracts`.

The Migration API provides explicit, opt-in helpers for upgrading
**contract-backed artifacts** between versions while preserving semantic intent.

Migration is a governance mechanism, not a convenience feature.

---

## Scope of this API

This API covers:

- Explicit migration helpers between contract versions
- Column mapping utilities used during migration
- Validation expectations before and after migration

It does *not* cover:

- Automatic or implicit upgrades
- Backward (new → old) migration guarantees
- Regeneration of artifacts from raw data
- Semantic inference or guessing

Migration is intentionally conservative.

---

## Why migration is explicit

In Electric Barometer (EB), contracts define **meaning**, not just structure.

Automatically coercing artifacts between versions risks:

- Silent semantic drift
- Loss of historical comparability
- Undetected misalignment downstream

Therefore, EB enforces a strict rule:

> **All migrations must be explicit, visible, and validated.**

---

## Public entrypoints

Migration helpers are exposed through the `eb_contracts.migrate` namespace.

Consumers should not implement ad-hoc migrations outside this API
for contract-backed artifacts.

---

## Supported migration types

Migration utilities are provided selectively and intentionally.

Typical supported scenarios include:

- Canonical column renaming with unchanged semantics
- Panel shape normalization without reinterpretation
- Alignment of legacy naming conventions to EB standards

If semantic meaning changes, migration may not be supported.

---

## Forecast migration helpers

Forecast artifacts are the primary focus of migration support.

Migration helpers may:

- Map legacy forecast columns to canonical EB columns
- Enforce explicit horizon semantics
- Normalize panel representations

Forecast migration targets are explicit (e.g. `v1` → `v2`).

---

## Column mapping specifications

Many migrations rely on **explicit column mapping definitions**.

These mappings:

- Declare source → target column relationships
- Are reviewed as part of migration logic
- Prevent implicit or heuristic-based inference

If a column cannot be mapped safely, migration must fail.

---

## Required migration workflow

The required workflow for migration is:

1. Start with an artifact valid under its source contract
2. Invoke an explicit migration helper
3. Receive a transformed artifact
4. Validate against the target contract version
5. Address any validation failures

Migration does not bypass validation.

---

## Validation behavior

Migrated artifacts must pass validation under the **target contract**.

Validation checks:

- Schema and column correctness
- Semantic consistency
- Numeric validity

Validation modes apply as usual:
- `strict` → errors
- `warn` → warnings
- `off` → no enforcement

Migration failures should not be suppressed.

---

## Versioning guarantees

Migration utilities follow these guarantees:

- Migration targets are explicit and versioned
- No implicit multi-step upgrades are performed
- Old migration paths may be deprecated but not altered

Migration logic itself is reviewed as contract-critical code.

---

## When migration is not provided

Migration helpers are intentionally *not* provided when:

- Semantics fundamentally change
- Artifacts must be regenerated upstream
- Meaning cannot be preserved safely

In these cases, regeneration is the correct approach.

---

## Failure philosophy

Migration failures are a **feature**, not a bug.

A failure indicates:

- Ambiguous semantics
- Unsafe assumptions
- Incompatible historical artifacts

Failing early protects downstream correctness.

---

## Relationship to versioning

Versioning defines *what changed*.
Migration defines *how (or whether) to move forward*.

The two are tightly coupled but distinct.

See:
- `concepts/versioning.md`
- `guides/migration.md`

---

## Design principles

The Migration API follows these principles:

- **Explicit over automatic**
- **Semantic safety over convenience**
- **Validation as a gate**
- **User acknowledgment of change**
- **No silent coercion**

---

## Summary

The Migration API enables **controlled evolution** of EB contracts.

It ensures that upgrades are intentional, auditable,
and semantically safe — preserving trust in both historical
and future Electric Barometer artifacts.

Migrate deliberately. Validate always.
