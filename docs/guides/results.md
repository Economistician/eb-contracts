# Result Contracts

This guide documents **result artifact contracts** in `eb-contracts`.

Result contracts formalize the **alignment of predictions and actuals**
into a single, validated artifact that can be safely consumed by
evaluation, metrics, optimization, and decision layers in
Electric Barometer (EB).

---

## Why result contracts exist

Forecasts and actuals are often joined informally:

- Joins rely on implicit keys
- Horizon semantics are misapplied
- Leakage occurs silently
- Evaluation logic compensates ad hoc

Result contracts eliminate these risks by making **alignment explicit,
validated, and versioned**.

If an artifact validates as a result contract, prediction–actual alignment
is guaranteed.

---

## What a result contract represents

A result contract represents:

- A forecasted value
- The corresponding realized actual value
- A shared entity, interval, and horizon context
- A single, interpretable unit of comparison

It does *not*:

- Compute metrics
- Apply costs
- Optimize decisions

Result contracts are the **boundary between data preparation and evaluation**.

---

## Panel result artifacts

EB uses **panel-style result artifacts**.

Each row represents a single comparison for a specific:

- Entity
- Interval or target period
- Forecast horizon
- Prediction–actual pair

This mirrors the structure of panel forecasts,
with actuals introduced explicitly.

---

## PanelPointResultV1

`PanelPointResultV1` is the canonical result contract for
point forecast evaluation.

Key characteristics:

- One predicted value per row
- One realized actual value per row
- Explicit alignment across entity, interval, and horizon
- Validated numeric consistency

This contract is intentionally minimal and strict.

---

## Canonical alignment semantics

Result contracts enforce alignment rules such as:

- Predictions and actuals refer to the same target interval
- Horizons are interpreted consistently
- Entities are matched exactly
- No many-to-many joins are allowed

If alignment cannot be proven, validation fails.

---

## Validation behavior

Result contracts are validated across multiple dimensions:

- **Schema** – required columns and types
- **Alignment** – prediction–actual correspondence
- **Semantics** – horizon and interval meaning
- **Numerics** – valid numeric values

Validation modes (`strict`, `warn`, `off`) apply uniformly,
allowing flexibility across environments.

---

## Relationship to forecasts

Result artifacts are produced *from* forecasts.

Typical flow:

1. Validate a forecast artifact
2. Join with realized actuals
3. Construct a result artifact
4. Validate the result contract
5. Pass downstream for evaluation

Forecast validation does not guarantee result validity;
alignment is a separate contract boundary.

---

## Relationship to costs and metrics

Result contracts are consumed by:

- Cost-weighted metrics
- Symmetric error metrics
- Readiness and service loss frameworks

Costs and metrics **assume** result validity.
They do not defend against misalignment.

---

## Leakage prevention

Result contracts are a primary defense against leakage.

They prevent:

- Using future actuals inadvertently
- Mixing horizons across joins
- Aggregating mismatched entities
- Double-counting comparisons

If a result validates, these errors cannot occur silently.

---

## Versioning and evolution

Result contracts are versioned explicitly.

Rules:

- Semantic alignment changes require a new version
- Additive fields must not affect interpretation
- Old versions remain supported for historical artifacts

Consumers should rely on stable validation entrypoints.

---

## When to create a new result version

A new version is appropriate when:

- Alignment semantics change
- Additional dimensions of comparison are introduced
- Existing guarantees are insufficient

If meaning changes, version must change.

---

## Design principles

Result contracts follow these principles:

- **Explicit alignment**
- **Leakage prevention**
- **Semantic clarity**
- **Versioned guarantees**
- **Evaluation safety**

---

## Summary

Result contracts are the **evaluation boundary** of Electric Barometer.

They ensure that every metric, loss, or decision is based on
correctly aligned predictions and actuals — no exceptions,
no hidden assumptions.

Treat results as contracts, not joins.
