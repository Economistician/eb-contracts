# Costs API

This document describes the **public API surface** for cost specification
contracts exposed by `eb-contracts`.

The Costs API provides stable constructors and validation entrypoints for
encoding **asymmetric cost assumptions** used throughout the
Electric Barometer (EB) ecosystem.

---

## Scope of this API

This API covers:

- Construction of cost specification artifacts
- Validation rules and guarantees
- Versioning and stability expectations

It does *not* cover:

- Metric computation
- Loss function definitions
- Optimization logic
- Currency or absolute economic modeling

Those concerns are intentionally handled downstream.

---

## Public entrypoints

All external consumers must use **stable validation entrypoints**
exposed via:

```python
from eb_contracts import validate
```

Do not import versioned cost classes (`v1`, `v2`) directly.
They are internal implementation details.

---

## `cost_asymmetry_v1`

```python
cost_asymmetry_v1(
    *,
    under_cost: float,
    over_cost: float,
    **kwargs,
) -> CostAsymmetrySpecV1
```

Constructs and validates a **CostAsymmetrySpecV1** artifact.

---

## Parameters

### `under_cost` (required)

Relative cost applied when **under-forecasting**
(prediction < actual).

Requirements:
- Must be a finite, positive number
- Interpreted relative to `over_cost`

---

### `over_cost` (required)

Relative cost applied when **over-forecasting**
(prediction > actual).

Requirements:
- Must be a finite, positive number
- Interpreted relative to `under_cost`

---

### Additional keyword fields

Optional, contract-defined metadata fields may be provided.

Examples:
- `name`
- `description`
- `scenario`

Only fields explicitly defined by the contract are accepted.
Unexpected fields trigger validation violations.

---

## Return value

Returns a validated **CostAsymmetrySpecV1** object.

Guarantees:
- Cost parameters are present and valid
- Directional semantics are explicit
- Interpretation is stable across systems

If validation fails, behavior depends on the active validation mode.

---

## Validation behavior

Cost artifacts are validated using the standard EB runtime.

Validation includes:

- Presence of required parameters
- Positivity and numeric validity
- Semantic interpretability of cost direction

Validation modes apply uniformly:
- `strict` → errors
- `warn` → warnings
- `off` → no enforcement

---

## Example usage

```python
from eb_contracts.validate import cost_asymmetry_v1

costs = cost_asymmetry_v1(
    under_cost=2.0,
    over_cost=1.0,
    name="understock_penalty",
)
```

This indicates that under-forecasting is twice as costly
as over-forecasting.

---

## Relationship to metrics

Cost contracts do not compute metrics.

Instead, they are consumed by metrics such as:

- Cost-weighted service loss
- Asymmetric error penalties
- Readiness and decision scoring

Metrics assume that cost artifacts are already validated
and semantically correct.

---

## Relationship to optimization

Optimization and policy layers may:

- Convert cost ratios into objective weights
- Combine cost specs with forecasts and results
- Reason about trade-offs explicitly

They must not reinterpret or mutate contract semantics.

---

## Versioning guarantees

For `CostAsymmetrySpecV1`:

- Directional meaning will not change
- Required parameters will not be removed
- Validation rules will not tighten silently

Any semantic change requires a new major version.

---

## Migration considerations

Cost semantics are difficult to migrate safely.

If interpretation changes:
- A new major version will be introduced
- Migration utilities may not be provided
- Historical cost specs remain valid under their original version

---

## Error handling

If validation fails:

- `strict` mode raises an exception
- `warn` mode emits warnings
- `off` mode bypasses validation

Consumers should not suppress cost validation failures,
as they directly affect downstream decisions.

---

## Design principles

The Costs API follows these principles:

- **Explicit asymmetry**
- **Relative, not absolute, costs**
- **Stable semantics**
- **Downstream interpretability**
- **Versioned guarantees**

---

## Summary

The Costs API provides a stable, validated interface for expressing
asymmetric cost assumptions in Electric Barometer.

By encoding cost semantics explicitly and versioning them carefully,
EB ensures that economic assumptions are transparent,
auditable, and consistently applied across the system.

Treat costs as contracts — not tuning parameters.
