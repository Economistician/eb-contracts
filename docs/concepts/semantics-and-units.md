# Semantics and Units

This document explains how **semantics** and **units** are defined, enforced,
and versioned in `eb-contracts`.

Semantics and units ensure that numeric values in Electric Barometer (EB)
artifacts are not only valid, but **meaningful and interpretable** across
systems, time, and use cases.

---

## Why semantics and units matter

A number without meaning is dangerous.

In data systems, the most costly failures often occur when:

- Numbers are technically valid but semantically wrong
- Units are assumed instead of specified
- Different systems interpret the same value differently
- Aggregations mix incompatible quantities

EB treats semantics and units as **first-class contract components**
to prevent these failures.

---

## Semantics vs units

Semantics and units are related but distinct.

---

### Semantics

*Semantics* describe **what a value represents**.

Examples:
- A forecasted demand value
- A realized actual count
- A cost ratio
- A probability or quantile

Semantics answer the question:
> *“What does this number mean?”*

---

### Units

*Units* describe **how a value is measured**.

Examples:
- Counts
- Rates
- Percentages
- Ratios
- Dimensionless quantities

Units answer the question:
> *“In what scale or measurement is this value expressed?”*

A value is only interpretable when both are known.

---

## Semantics as part of the contract

In `eb-contracts`, semantics are not implied by context.
They are explicitly defined as part of the contract.

This means:

- Changing a value’s meaning requires a new contract version
- Reusing a column name with different semantics is forbidden
- Downstream systems may rely on semantic guarantees

Semantics are as stable and versioned as schemas.

---

## Units as guarantees

Units define **what operations are valid**.

For example:

- Counts may be summed
- Ratios may not be summed meaningfully
- Percentages require normalization
- Dimensionless values must be interpreted carefully

By defining units explicitly, EB prevents invalid mathematical operations
from being applied downstream.

---

## Common EB semantic categories

While exact definitions live in code, EB semantics commonly include:

- **Predictions** – forecasted quantities
- **Actuals** – realized outcomes
- **Costs** – relative penalties or weights
- **Identifiers** – non-numeric reference values
- **Probabilities / quantiles** – distributional descriptors

Each category has different interpretability rules.

---

## Dimensionless values

Not all numeric values have physical units.

Examples:
- Cost ratios
- Quantiles
- Readiness scores

These values are still governed semantically:

- Valid ranges are enforced
- Interpretability is defined
- Comparability rules are explicit

Dimensionless does not mean unconstrained.

---

## Validation of semantics and units

Validation enforces semantic and unit correctness by checking:

- Numeric ranges (e.g. probabilities in [0, 1])
- Prohibited values (e.g. negative counts)
- Consistency across related columns
- Compatibility with contract definitions

Validation catches errors that schema checks cannot.

---

## Relationship to canonical columns

Canonical columns define **where values live**.
Semantics and units define **what those values mean**.

Together, they ensure:

- Column names are interpretable
- Values are comparable
- Downstream logic is safe

Neither is sufficient alone.

---

## Versioning rules

Semantics and units are versioned with their contracts.

Rules:

- Changing semantics requires a new major version
- Tightening valid ranges requires a new version
- Clarifications may be documented without version changes
- Backward compatibility is prioritized

Semantic stability is treated as a product guarantee.

---

## Migration considerations

When semantics or units change:

- Migration utilities may be unsafe or impossible
- Artifacts may need to be regenerated upstream
- Silent conversion is explicitly forbidden

Meaning cannot be inferred automatically.

---

## Anti-patterns

Avoid:

- Assuming units based on context
- Mixing semantically different values in one column
- Overloading numeric columns with flags or encodings
- Converting units implicitly

If meaning matters, it must be explicit.

---

## Design principles

Semantics and units in EB follow these principles:

- **Meaning before math**
- **Explicit interpretation**
- **Versioned guarantees**
- **Downstream safety**
- **No implicit assumptions**

---

## Summary

Semantics and units are how Electric Barometer ensures that numbers
are not just valid — they are *understood*.

By encoding meaning directly into contracts,
EB prevents subtle, costly errors that schema validation alone cannot catch.

If a value’s meaning matters, the contract must say so.
