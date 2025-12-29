# Validation API

This document describes the **public validation entrypoints** exposed by
`eb-contracts`.

The Validation API is the **only supported public surface** for constructing
and validating Electric Barometer (EB) artifacts. It defines how raw data
becomes **contract-backed, trustworthy artifacts**.

---

## Scope of this API

This API covers:

- Stable constructors for all contract-backed artifacts
- Validation guarantees and failure behavior
- Version routing and public surface stability

It does *not* cover:

- Contract internals or versioned class implementations
- Migration logic
- Runtime configuration (see `api/runtime.md`)
- Metric, evaluation, or optimization logic

If an artifact enters EB, it should enter through this API.

---

## Why a validation API exists

Directly importing versioned contract classes couples consumers to
implementation details and breaks stability guarantees.

The Validation API exists to:

- Provide a **stable, minimal public surface**
- Route to correct contract versions internally
- Enforce consistent validation behavior
- Protect consumers from structural churn

This is the contract boundary of the EB ecosystem.

---

## Stable entrypoint rule

> **All external consumers must use `eb_contracts.validate`.**

Consumers must not:
- Import versioned modules (`v1`, `v2`) directly
- Instantiate contract classes manually
- Bypass validation at artifact boundaries

Stable entrypoints are the only supported integration path.

---

## Artifact constructors

Each validation function:

- Accepts raw inputs (usually a pandas DataFrame or keyword args)
- Performs contract validation
- Returns a contract-backed artifact on success

---

## Forecast validation entrypoints

### `panel_point_v1`

```python
panel_point_v1(
    frame: pandas.DataFrame,
)
```

Validates and constructs a **panel point forecast** artifact.

See:
- `api/forecast.md`
- `guides/forecasts.md`

---

### `panel_quantile_v1`

```python
panel_quantile_v1(
    frame: pandas.DataFrame,
)
```

Validates and constructs a **panel quantile forecast** artifact.

---

## Cost validation entrypoints

### `cost_asymmetry_v1`

```python
cost_asymmetry_v1(
    *,
    under_cost: float,
    over_cost: float,
    **kwargs,
)
```

Validates and constructs a **cost asymmetry specification** artifact.

See:
- `api/costs.md`
- `guides/costs.md`

---

## Result validation entrypoints

### `panel_point_result_v1`

```python
panel_point_result_v1(
    frame: pandas.DataFrame,
)
```

Validates and constructs a **panel point result** artifact.

See:
- `api/results.md`
- `guides/results.md`

---

## Context validation entrypoints

### `run_context_v1`

```python
run_context_v1(
    *,
    run_id: str,
    **kwargs,
)
```

Validates and constructs a **run context** artifact.

See:
- `api/context.md`
- `guides/context.md`

---

## Validation guarantees

If a validation function returns successfully:

- Schema requirements are satisfied
- Semantic meaning is unambiguous
- Units and numeric constraints are respected
- Downstream systems may assume correctness

If validation fails, the artifact must not proceed downstream.

---

## Failure behavior

Failure behavior depends on the active validation mode:

- `strict` → raise exceptions
- `warn` → emit warnings and continue
- `off` → bypass enforcement

See:
- `api/runtime.md`
- `getting-started/validation-modes.md`

---

## Error signaling

Validation failures:

- Are deterministic
- Are specific and actionable
- Indicate boundary violations, not downstream bugs

Consumers must not suppress or reinterpret validation failures silently.

---

## Version routing

Stable entrypoints may route to:

- Different internal contract versions
- Updated implementations
- Extended validation logic

This routing is transparent to consumers and preserves stability.

---

## Relationship to migration

Validation and migration are distinct:

- Validation checks correctness under a given version
- Migration transforms artifacts between versions

Validation must always occur **after** migration.

See:
- `api/migrate.md`
- `guides/migration.md`

---

## Intended usage pattern

A correct EB workflow:

1. Produce or ingest raw data
2. Validate using the Validation API
3. Pass validated artifacts downstream
4. Avoid re-validation or reshaping internally

This pattern enforces trust at boundaries and simplicity inside systems.

---

## Anti-patterns

Avoid:

- Instantiating contract classes directly
- Bypassing validation at system boundaries
- Catching and suppressing validation errors
- Treating validation as optional

If validation is skipped, guarantees are lost.

---

## Design principles

The Validation API follows these principles:

- **Single public entrypoint**
- **Explicit boundary enforcement**
- **Stable version routing**
- **Semantic guarantees**
- **Fail-fast defaults**

---

## Summary

The Validation API is the **front door** of Electric Barometer.

If data enters EB through this API, it is trusted.
If it does not, it is not an EB artifact.

Validate once.
Trust everywhere.
