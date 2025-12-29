# Canonical Columns

This document defines the concept of **canonical columns** in `eb-contracts`
and explains why column naming is treated as a first-class, versioned concern
in the Electric Barometer (EB) ecosystem.

Canonical columns are not stylistic conventions — they are **semantic contracts**.

---

## What are canonical columns?

Canonical columns are the **official, contract-defined column names**
used by EB artifacts.

They specify:

- What information a column represents
- How that information is interpreted semantically
- How artifacts can be joined, aligned, and validated
- What downstream systems are allowed to assume

If a column is canonical, its name and meaning are stable within a contract version.

---

## Why canonical columns matter

In many data systems, column names are informal and contextual.
In EB, this is unacceptable.

Canonical columns exist to prevent:

- Ambiguous joins
- Implicit assumptions about time or entity meaning
- Inconsistent naming across teams
- Silent semantic drift

A validated EB artifact is not just structurally correct —
it is **semantically interpretable** because its columns are canonical.

---

## Columns as part of the contract

In `eb-contracts`, column definitions are part of the contract itself.

This means:

- Renaming a canonical column is a breaking change
- Changing a column’s meaning requires a new contract version
- Adding optional canonical columns is treated cautiously

Columns are governed with the same rigor as schemas and validation logic.

---

## Categories of canonical columns

Canonical columns fall into several conceptual categories.

---

### Entity identifiers

These columns define *what* the data refers to.

Examples:
- Store identifiers
- Region identifiers
- Product or SKU identifiers

Entity columns must be:

- Explicit
- Stable
- Unambiguous

---

### Temporal columns

These columns define *when* the data applies.

Examples:
- Target dates or intervals
- Observation timestamps
- Forecast horizons

Temporal columns are especially sensitive to semantic drift
and are validated aggressively.

---

### Prediction and outcome columns

These columns define *what is being predicted or measured*.

Examples:
- Forecasted values
- Realized actual values
- Quantile predictions

Prediction and outcome columns must have clear units
and consistent numeric interpretation.

---

### Auxiliary and metadata columns

Some canonical columns provide supporting structure.

Examples:
- Quantile identifiers
- Horizon indicators
- Scenario labels (when explicitly part of the contract)

Only explicitly defined auxiliary columns are permitted.

---

## Canonical vs non-canonical columns

Not every column belongs in a contract.

Canonical columns:
- Are required or explicitly allowed
- Have defined semantics
- Are validated

Non-canonical columns:
- Are ignored by validation
- Must not affect interpretation
- Should not be relied upon by downstream systems

If a column affects meaning, it must be canonical.

---

## Relationship to semantics and units

Canonical columns define **structure**;
semantic descriptors and units define **meaning**.

Together, they ensure:

- A column’s numeric values are interpretable
- Units are consistent across artifacts
- Downstream computations are valid

Canonical columns without semantics are incomplete.

---

## Versioning rules

Canonical columns are versioned with their contracts.

Rules:

- Removing a required canonical column requires a new version
- Renaming a canonical column requires a new version
- Changing semantic meaning requires a new version
- Adding optional columns must not affect interpretation

Stability is prioritized over convenience.

---

## Migration considerations

When canonical columns change between versions:

- Migration utilities may be provided
- Column mapping must be explicit
- Ambiguous mappings must fail

Automatic inference is intentionally avoided.

---

## Anti-patterns

Avoid:

- Aliasing canonical columns silently
- Overloading one column with multiple meanings
- Encoding semantics in column names ad hoc
- Adding operational metadata as canonical columns

These patterns undermine contract integrity.

---

## Design principles

Canonical columns follow these principles:

- **One column, one meaning**
- **Explicit naming**
- **Versioned stability**
- **Semantic clarity**
- **Downstream safety**

---

## Summary

Canonical columns are the vocabulary of Electric Barometer.

They define how data speaks across systems.
Once validated, their meaning is guaranteed.

Treat column names as contracts — because they are.
