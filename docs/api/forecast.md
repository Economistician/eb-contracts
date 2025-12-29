# Forecast API

This document describes the **public API surface** for forecast contracts
exposed by `eb-contracts`.

The Forecast API provides stable constructors and validation entrypoints for
**panel-style forecast artifacts** used throughout the Electric Barometer (EB)
ecosystem.

---

## Scope of this API

This API covers:

- Construction of forecast artifacts
- Validation rules and guarantees
- Versioning and stability expectations

It does *not* cover:

- Model training or inference
- Feature engineering
- Forecast generation logic
- Metric computation or decisioning

Those concerns are intentionally handled by downstream systems.

---

## Public entrypoints

All external consumers must use the **stable validation entrypoints**
exposed via:

```python
from eb_contracts import validate
```

Do not import versioned forecast classes (`v1`, `v2`) directly.
They are internal implementation details.

---

## Panel-style forecasts

All EB forecast contracts use a **panel representation**.

Each row represents a single forecast for a specific:

- Entity
- Target interval
- Forecast horizon
- (Optional) quantile

Panel structure is enforced and validated.

---

## `panel_point_v1`

```python
panel_point_v1(
    frame: pandas.DataFrame,
) -> PanelPointForecastV1
```

Validates and constructs a **panel point forecast** artifact.

---

## Parameters

### `frame` (required)

A pandas DataFrame containing forecast data.

Requirements:
- Must contain all required canonical columns
- Must conform to panel structure expectations
- Must contain exactly one prediction value per row

Column names and semantics are defined by the contract.

---

## Return value

Returns a validated **PanelPointForecastV1** object.

Guarantees:
- Schema correctness
- Semantic interpretability
- Panel alignment consistency

If validation fails, behavior depends on the active validation mode.

---

## `panel_quantile_v1`

```python
panel_quantile_v1(
    frame: pandas.DataFrame,
) -> PanelQuantileForecastV1
```

Validates and constructs a **panel quantile forecast** artifact.

---

## Quantile-specific behavior

For quantile forecasts:

- Quantile column is required
- Quantile values must be within valid bounds
- Each entity–interval–horizon–quantile combination must be unique

Quantiles are explicit and validated — never inferred.

---

## Validation behavior

Forecast artifacts are validated across multiple dimensions:

- Required columns and types
- Panel shape consistency
- Horizon and temporal semantics
- Numeric validity of predictions
- Quantile constraints (when applicable)

Validation modes apply uniformly:
- `strict` → errors
- `warn` → warnings
- `off` → no enforcement

---

## Example: point forecast

```python
from eb_contracts.validate import panel_point_v1

forecast = panel_point_v1(df)
```

After validation, the artifact can be consumed safely downstream.

---

## Example: quantile forecast

```python
from eb_contracts.validate import panel_quantile_v1

forecast = panel_quantile_v1(df)
```

Quantile semantics are guaranteed by the contract.

---

## Relationship to results

Forecast artifacts define **predictions only**.

To evaluate forecasts:

1. Validate a forecast artifact
2. Join with realized actuals
3. Construct a result artifact
4. Pass results to metrics or optimization

Forecast validity does not imply result validity.

---

## Versioning guarantees

For forecast contracts:

- Column semantics remain stable within a version
- Panel interpretation does not change silently
- Validation rules do not tighten without a new major version

New versions are introduced only for semantic change.

---

## Migration considerations

Migration utilities may be provided when:

- Column names change without semantic change
- Panel shape is refined safely

If meaning changes, artifacts must be regenerated upstream.

---

## Error handling

If validation fails:

- `strict` mode raises an exception
- `warn` mode emits warnings
- `off` mode bypasses validation

Forecast validation failures must not be suppressed,
as they directly affect downstream correctness.

---

## Design principles

The Forecast API follows these principles:

- **Panel-first representation**
- **Explicit structure and semantics**
- **Stable public entrypoints**
- **Versioned guarantees**
- **Downstream safety**

---

## Summary

The Forecast API provides a stable, validated interface for representing
predictions in Electric Barometer.

By enforcing panel structure, explicit semantics, and strict validation,
it ensures that forecasts entering the system are trustworthy,
interpretable, and safe to consume everywhere downstream.

Treat forecasts as contracts — not loose DataFrames.
