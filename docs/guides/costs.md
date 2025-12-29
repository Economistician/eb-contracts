# Cost Contracts

This guide documents **cost specification contracts** in `eb-contracts`.

Cost contracts formalize how **asymmetric costs** are represented, validated,
and communicated across the Electric Barometer (EB) ecosystem.

They provide a canonical, interpretable interface between forecasting,
evaluation, and optimization layers.

---

## Why cost contracts exist

Electric Barometer is explicitly **cost-aware**.

Forecast error is not symmetric:
- Over-forecasting and under-forecasting incur different real-world costs
- Those costs vary by context, use case, and decision horizon

Without explicit cost contracts, systems implicitly assume symmetry or
hard-code assumptions that are invisible and fragile.

Cost contracts make cost assumptions:
- **Explicit**
- **Versioned**
- **Auditable**
- **Reusable across systems**

---

## What a cost contract represents

A cost contract defines how forecast error should be **penalized relative to direction**.

It does *not*:
- Compute loss values
- Enforce a specific metric
- Encode business rules directly

Instead, it specifies **cost asymmetry parameters**
that downstream components (metrics, optimization, policies) interpret consistently.

---

## CostAsymmetrySpecV1

`CostAsymmetrySpecV1` is the canonical cost specification contract.

It represents the **relative cost of under-forecasting vs over-forecasting**
in a normalized, interpretable form.

Key characteristics:

- Explicit versioning (`v1`)
- Schema-validated parameters
- Directionally interpretable semantics
- Compatible with EB cost-weighted metrics

---

## Core concepts

### Under vs over forecasting

Cost asymmetry is defined with respect to **forecast error direction**:

- **Under-forecasting**: prediction < actual
- **Over-forecasting**: prediction > actual

The contract encodes how costly each direction is *relative to the other*.

---

### Cost ratios, not absolutes

Cost contracts specify **relative costs**, not absolute currency values.

This allows:

- Scale invariance across entities
- Comparability across experiments
- Separation of economic modeling from statistical modeling

Absolute cost modeling belongs downstream, not in the contract layer.

---

## Typical fields

While exact fields are defined in code, a typical cost specification includes:

- Parameters describing under-forecast cost weight
- Parameters describing over-forecast cost weight
- Optional identifiers or annotations

All fields are validated for:

- Presence
- Type correctness
- Semantic validity (e.g. positivity, interpretability)

---

## Validation behavior

Cost contracts are validated like all EB contracts.

Validation ensures:

- Required parameters are present
- Cost parameters are numerically valid
- Semantics are consistent with EB expectations

Validation modes (`strict`, `warn`, `off`) apply uniformly, allowing:

- Strict enforcement in CI and production
- Leniency in exploratory research

---

## Using cost contracts downstream

Cost contracts are designed to be **consumed, not transformed**.

Downstream systems may:

- Convert cost ratios into metric weights
- Use cost asymmetry in loss functions
- Incorporate costs into optimization objectives

But they should not reinterpret or mutate the contract semantics.

---

## Relationship to metrics

Cost contracts do not define metrics, but metrics rely on them.

Examples:

- Cost-weighted service loss metrics
- Asymmetric error penalties
- Decision readiness scoring

By separating *cost definition* from *metric computation*,
EB ensures consistency across implementations.

---

## Versioning and stability

For `CostAsymmetrySpecV1`, the following guarantees hold:

- No semantic reinterpretation of cost direction
- No renaming of core parameters
- No tightening of validation rules without version bump

Breaking changes require a new major version.

---

## When to create a new cost contract

A new version is warranted when:

- The meaning of cost direction changes
- Additional dimensions of cost are introduced
- Existing parameters can no longer express required behavior

Additive extensions should prefer new optional fields
or parallel contract families.

---

## Design principles

Cost contracts follow these principles:

- **Explicit asymmetry**
- **Semantic clarity**
- **Versioned stability**
- **Metric-agnostic design**
- **Downstream interpretability**

---

## Summary

Cost contracts are the economic backbone of Electric Barometer.

They ensure that asymmetric decision costs are encoded once,
validated once, and interpreted consistently everywhere.

Treat cost specifications as contracts, not configuration.
