# Context API

This document describes the **public API surface** for run context contracts
exposed by `eb-contracts`.

The Context API provides stable constructors and validation entrypoints for
**run-level metadata** used throughout the Electric Barometer (EB) ecosystem.

---

## Scope of this API

This API covers:

- Construction of run context artifacts
- Validation behavior and guarantees
- Stability and versioning expectations

It does *not* cover:

- Storage or serialization formats
- Transport mechanisms
- Application-specific metadata handling

Those concerns are intentionally left to downstream systems.

---

## Public entrypoints

All external consumers should use the **stable validation entrypoints**
defined in `eb_contracts.validate`.

Do not import versioned context classes directly.

---

## `run_context_v1`

```python
run_context_v1(
    *,
    run_id: str,
    **kwargs,
) -> RunContextV1
```

Constructs and validates a **RunContextV1** artifact.

---

## Parameters

### `run_id` (required)

A unique identifier for the execution or run.

Requirements:
- Must be a non-empty string
- Must uniquely identify the producing run within its scope

---

### Additional keyword fields

Additional fields may be provided depending on the contract definition.

Examples:
- `environment`
- `pipeline`
- `model_id`
- `scenario`
- `notes`

Only fields explicitly defined by the contract are accepted.
Unexpected fields will trigger validation violations.

---

## Return value

Returns a validated **RunContextV1** object.

Guarantees:
- All required fields are present
- Field types are correct
- Semantic constraints are satisfied

If validation fails, behavior depends on the active validation mode.

---

## Validation behavior

Context artifacts are validated using the same runtime as all EB contracts.

Validation checks include:

- Required field presence
- Type correctness
- Semantic validity
- Disallowed or unknown fields

Validation modes apply uniformly:
- `strict` → errors
- `warn` → warnings
- `off` → no enforcement

---

## Example usage

```python
from eb_contracts.validate import run_context_v1

context = run_context_v1(
    run_id="forecast-run-2025-01-01",
    environment="prod",
    pipeline="daily-forecast",
    model_id="xgb_v3",
)
```

The returned object can be attached to or associated with other EB artifacts.

---

## Relationship to other artifacts

Run context is **orthogonal** to tabular artifacts.

It may be associated with:
- Forecast artifacts
- Result artifacts
- Evaluation outputs
- Optimization decisions

But it must not alter or reshape their schemas.

---

## Versioning guarantees

For `RunContextV1`:

- Required fields will not be removed
- Field semantics will not change silently
- Validation rules will not tighten without a new major version

New optional fields may be introduced cautiously.

---

## Migration considerations

Context contracts evolve conservatively.

If semantics change:
- A new major version will be introduced
- Migration utilities may not be provided
- Historical contexts remain valid under their original version

---

## Error handling

If validation fails:

- In `strict` mode, an exception is raised
- In `warn` mode, warnings are emitted
- In `off` mode, validation is bypassed

Consumers should not suppress or reinterpret context validation failures.

---

## Design principles

The Context API follows these principles:

- **Explicit metadata**
- **Separation of concerns**
- **Stable public surface**
- **Versioned semantics**
- **Attachable, not embedded**

---

## Summary

The Context API provides a stable, validated interface for run-level metadata
in Electric Barometer.

It ensures that provenance and execution context are explicit,
auditable, and semantically consistent across the ecosystem.

Use context to explain *how* artifacts were produced —
without contaminating *what* the data means.
