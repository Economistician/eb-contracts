# Results API

This document describes the **public API surface** for result artifact contracts
exposed by `eb-contracts`.

The Results API provides stable constructors and validation entrypoints for
**aligned prediction–actual artifacts** used by evaluation, metrics,
optimization, and decision layers in the Electric Barometer (EB) ecosystem.

---

## Scope of this API

This API covers:

- Construction of result artifacts
- Validation rules for prediction–actual alignment
- Versioning and stability guarantees

It does *not* cover:

- Metric computation
- Cost application
- Aggregation or reporting logic
- Optimization or policy decisions

Results define *comparability*, not *conclusions*.

---

## Public entrypoints

All external consumers must use the **stable validation entrypoints**
exposed via:

```python
from eb_contracts import validate
```

Do not import versioned result classes directly.
They are internal implementation details.

---

## Panel-style results

All EB result contracts use a **panel representation**.

Each row represents a single comparison for a specific:

- Entity
- Target interval
- Forecast horizon
- Prediction–actual pair

This structure mirrors panel forecasts with actuals added explicitly.

---

## `panel_point_result_v1`

```python
panel_point_result_v1(
    frame: pandas.DataFrame,
) -> PanelPointResultV1
```

Validates and constructs a **panel point result** artifact.

---

## Parameters

### `frame` (required)

A pandas DataFrame containing aligned prediction and actual values.

Requirements:
- Must contain all required canonical columns
- Must include both prediction and actual fields
- Must conform to panel alignment rules
- Must not introduce many-to-many joins

Column names and semantics are defined by the contract.

---

## Return value

Returns a validated **PanelPointResultV1** object.

Guarantees:
- Correct prediction–actual alignment
- Consistent horizon and temporal semantics
- Numeric validity of values
- Safety for downstream evaluation

If validation fails, behavior depends on the active validation mode.

---

## Validation behavior

Result artifacts are validated across multiple dimensions:

- Schema correctness
- Alignment guarantees
- Horizon and interval semantics
- Numeric validity of predictions and actuals

Validation modes apply uniformly:
- `strict` → errors
- `warn` → warnings
- `off` → no enforcement

Alignment violations must not be ignored.

---

## Example usage

```python
from eb_contracts.validate import panel_point_result_v1

results = panel_point_result_v1(df)
```

Once validated, the artifact can be passed safely to metrics and optimization.

---

## Relationship to forecasts

Result artifacts are produced *from* forecast artifacts.

Typical workflow:

1. Validate a forecast artifact
2. Join with realized actuals
3. Construct a result artifact
4. Validate the result contract
5. Consume downstream

Forecast validity alone does not guarantee result validity.

---

## Relationship to costs and metrics

Metrics and cost-weighted evaluation assume:

- Result artifacts are already validated
- Alignment semantics are correct
- No leakage is present

Results are the **evaluation boundary** of EB.

---

## Leakage prevention guarantees

Result contracts explicitly prevent:

- Using future actuals
- Mixing horizons incorrectly
- Double-counting comparisons
- Aggregating mismatched entities

If a result validates, these errors cannot occur silently.

---

## Versioning guarantees

For result contracts:

- Alignment semantics remain stable within a version
- Required fields are not removed silently
- Validation rules do not tighten without a new major version

Semantic change requires version change.

---

## Migration considerations

Migration utilities may be provided when:

- Column names change without semantic change
- Alignment structure is preserved

If interpretation changes, artifacts must be regenerated upstream.

---

## Error handling

If validation fails:

- `strict` mode raises an exception
- `warn` mode emits warnings
- `off` mode bypasses validation

Result validation failures indicate unsafe evaluation conditions
and must not be suppressed.

---

## Design principles

The Results API follows these principles:

- **Explicit alignment**
- **Leakage prevention**
- **Stable semantics**
- **Versioned guarantees**
- **Evaluation safety**

---

## Summary

The Results API provides a stable, validated interface for representing
prediction–actual alignment in Electric Barometer.

By enforcing explicit alignment and strict validation,
it ensures that every metric, loss, and decision is grounded
in correct and interpretable comparisons.

Treat results as contracts — not joins.
