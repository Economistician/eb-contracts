# Definitions API

This document describes the **definitions layer** exposed by `eb-contracts`.

The Definitions API provides the **canonical vocabulary** used by all Electric
Barometer (EB) contracts, including column names, semantic descriptors, and
unit annotations.

Definitions are not helpers or conveniences — they are **foundational
infrastructure** that ensures consistency and interpretability across the
entire EB ecosystem.

---

## Scope of this API

This API covers:

- Canonical column name definitions
- Semantic descriptors for values
- Unit annotations and constraints
- Shared constants used across contracts

It does *not* cover:

- Validation logic
- Artifact construction
- Business rules or transformations

Definitions are referenced by contracts; they do not enforce behavior directly.

---

## Why a definitions layer exists

Without a shared definitions layer:

- Column names drift across teams and repos
- Semantics are duplicated or reinterpreted
- Units are assumed rather than enforced
- Interoperability degrades over time

The Definitions API establishes a **single source of truth**
for how EB talks about data.

---

## Canonical column definitions

Canonical columns define **where information lives** in an artifact.

They specify:

- Column names
- Intended usage
- Structural role within a contract

Canonical columns are imported and reused across forecast, cost,
result, and context contracts.

Renaming or reinterpreting a canonical column is a breaking change.

---

## Semantic descriptors

Semantic descriptors define **what values mean**.

Examples of semantic categories:

- Predictions
- Actuals
- Costs
- Identifiers
- Probabilities / quantiles

Semantics are explicit and versioned.
They allow downstream systems to reason about values safely.

---

## Unit annotations

Unit annotations define **how values are measured**.

Examples:

- Counts
- Ratios
- Percentages
- Dimensionless quantities

Units constrain valid operations and valid numeric ranges.
They are essential for preventing invalid aggregation or comparison.

---

## Relationship between columns, semantics, and units

Definitions work as a cohesive system:

- Canonical columns define structure
- Semantics define meaning
- Units define measurement

All three are required for full interpretability.
None are sufficient alone.

---

## Usage by contracts

Contracts reference definitions to:

- Declare required columns
- Attach semantic meaning to fields
- Enforce numeric and unit constraints

This ensures consistent behavior across all contract families.

---

## Public vs internal usage

The Definitions API is **publicly readable** but not intended for mutation.

Consumers may:

- Reference definitions for inspection
- Use them to align external systems
- Generate documentation or tooling

Consumers must not:

- Override definitions
- Alias canonical names silently
- Reinterpret semantics locally

---

## Versioning guarantees

Definitions are versioned alongside contracts.

Rules:

- Semantic meaning does not change silently
- Canonical names remain stable within a version
- Changes require coordinated contract versioning

Definitions stability is treated as a system guarantee.

---

## Migration considerations

When definitions change:

- Migration utilities may reference old and new definitions
- Column mapping must be explicit
- Semantic ambiguity must be resolved manually

Automatic inference is explicitly avoided.

---

## Design principles

The Definitions API follows these principles:

- **Single source of truth**
- **Explicit semantics**
- **Unit-aware values**
- **Versioned stability**
- **Ecosystem-wide consistency**

---

## Summary

The Definitions API is the **shared language** of Electric Barometer.

By centralizing column names, semantics, and units,
it ensures that all EB contracts speak consistently —
across repositories, teams, and time.

Definitions are not optional.
They are how meaning stays intact.
