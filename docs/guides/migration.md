# Migration

This guide documents **migration utilities and principles** in `eb-contracts`.

Migration exists to support **intentional, explicit evolution** of contracts
without breaking historical artifacts or introducing silent semantic drift.

---

## Why migration is explicit

In Electric Barometer (EB), contracts define **meaning**, not just structure.
Automatically coercing old artifacts into new shapes risks changing semantics
without detection.

For this reason, EB follows a strict rule:

> **All migrations are explicit, opt-in, and documented.**

If an artifact changes meaning, that change must be acknowledged by the user.

---

## What migration means in eb-contracts

Migration is the process of:

- Transforming an artifact from one contract version to another
- Preserving semantic intent wherever possible
- Making any assumptions or reinterpretations explicit

Migration utilities exist to **assist**, not to hide change.

---

## What migration is NOT

Migration does *not*:

- Automatically upgrade artifacts at import time
- Silently coerce schemas between versions
- Guarantee semantic equivalence in all cases
- Replace validation

Every migrated artifact must still be validated against its target contract.

---

## Supported migration scenarios

Migration utilities are provided selectively.

Typical supported cases include:

- Renaming canonical columns with unchanged meaning
- Reformatting schema shapes without semantic reinterpretation
- Aligning legacy naming conventions to EB standards

If semantics change, migration may require manual intervention.

---

## Forecast artifact migration

Forecast contracts are the primary focus of migration support.

Forecast migration utilities may:

- Map legacy column names to canonical EB names
- Normalize panel shapes
- Enforce explicit horizon or target semantics

These utilities live under the `migrate` module and are version-aware.

---

## Column mapping helpers

Migration often relies on **explicit column mapping specifications**.

These mappings:

- Declare how source columns map to target contract columns
- Are reviewed as part of migration logic
- Prevent implicit assumptions

If a column cannot be mapped safely, migration should fail loudly.

---

## Validation after migration

Migration does not bypass validation.

Required flow:

1. Start with a valid artifact (source version)
2. Apply an explicit migration utility
3. Validate against the target contract version
4. Address any validation failures

If validation fails, the migration is incomplete or unsafe.

---

## Versioning rules for migration

Migration utilities follow these rules:

- Migration targets are explicit (`v1` → `v2`)
- No implicit multi-step upgrades
- No backward migration guarantees
- Deprecated paths are documented

Migration logic itself is versioned and reviewed carefully.

---

## When to add a migration utility

A migration utility is appropriate when:

- The new contract is strictly superior
- The old contract is widely used
- Semantics can be preserved or explicitly transformed

If migration requires guessing intent, it should not be automated.

---

## When NOT to migrate

Do not provide migration utilities when:

- Semantics fundamentally change
- Data must be re-derived upstream
- Business meaning shifts materially

In these cases, users should regenerate artifacts explicitly.

---

## Failure philosophy

Migration failures are a feature, not a bug.

A failed migration indicates:

- Ambiguous semantics
- Unsafe assumptions
- Incompatible historical data

Failing early protects downstream systems.

---

## Design principles

Migration in EB follows these principles:

- **Explicit over automatic**
- **Semantic safety over convenience**
- **Validation as a gate**
- **User acknowledgment of change**
- **No silent coercion**

---

## Summary

Migration utilities exist to support **controlled evolution** of EB contracts.

They make change visible, auditable, and intentional — preserving trust
in historical artifacts while allowing the ecosystem to grow.

Migrate carefully. Validate always.
