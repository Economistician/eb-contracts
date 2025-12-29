# API Reference

This page provides an overview of the **public API surface** exposed by
`eb-contracts`.

The API is intentionally small, stable, and explicit.
It exists to construct and validate **contract-backed artifacts**
used throughout the Electric Barometer (EB) ecosystem.

---

## Design goals of the API

The `eb-contracts` API is designed around a few core goals:

- **Stability** – public entrypoints do not change casually
- **Explicitness** – meaning is never inferred
- **Boundary enforcement** – validation happens at system edges
- **Semantic safety** – downstream systems can trust validated artifacts

If you are interacting with EB artifacts programmatically,
this API is your only supported entrypoint.

---

## Stable entrypoints

All public APIs are exposed via the `eb_contracts.validate` module.

```python
from eb_contracts import validate
```

Consumers should **never import versioned classes directly**
(e.g. `PanelPointForecastV1`).
Versioned modules are implementation details.

---

## Artifact families

The API is organized around distinct **artifact families**.
Each family defines a semantic boundary.

---

### Forecast artifacts

Forecast APIs construct and validate **panel-style forecasts**.

Entry points:

- `panel_point_v1`
- `panel_quantile_v1`

See:
- `api/forecast.md`
- `guides/forecasts.md`

---

### Cost artifacts

Cost APIs construct and validate **asymmetric cost specifications**.

Entry points:

- `cost_asymmetry_v1`

See:
- `api/costs.md`
- `guides/costs.md`

---

### Result artifacts

Result APIs construct and validate **aligned prediction–actual artifacts**
used for evaluation.

Entry points:

- `panel_point_result_v1`

See:
- `api/results.md`
- `guides/results.md`

---

### Context artifacts

Context APIs construct and validate **run-level metadata artifacts**.

Entry points:

- `run_context_v1`

See:
- `api/context.md`
- `guides/context.md`

---

## Validation runtime

Validation behavior is controlled globally via the validation runtime.

Key entrypoints:

- `set_validation_mode`

Validation modes:

- `strict`
- `warn`
- `off`

See:
- `getting-started/validation-modes.md`

---

## Definitions layer

The API relies on a shared **definitions layer** that provides:

- Canonical column names
- Semantic descriptors
- Unit annotations

Definitions are part of the public vocabulary but are not mutable.

See:
- `api/definitions.md`
- `concepts/canonical-columns.md`

---

## Versioning model

API entrypoints are versioned intentionally.

Rules:

- Versions encode semantic meaning, not code layout
- Breaking changes require new versions
- Old versions remain supported for historical artifacts

See:
- `concepts/versioning.md`
- `guides/migration.md`

---

## Error handling

All API functions perform validation.

Behavior depends on validation mode:

- `strict` → raise errors
- `warn` → emit warnings
- `off` → bypass enforcement

Errors indicate boundary violations and must not be suppressed.

See:
- `concepts/errors-and-violations.md`

---

## Intended usage pattern

A typical EB workflow using the API:

1. Produce or ingest raw data
2. Validate data using a contract API
3. Pass validated artifacts downstream
4. Avoid re-validation or reshaping internally

This pattern ensures correctness, clarity, and interoperability.

---

## What the API does NOT do

The API does not:

- Train models
- Generate forecasts
- Compute metrics
- Optimize decisions
- Store or transport artifacts

It defines **what data means**, not **what systems do with it**.

---

## Design principles

The API follows these principles:

- **Small public surface**
- **Stable entrypoints**
- **Explicit versioning**
- **Semantic guarantees**
- **Boundary-first validation**

---

## Summary

The `eb-contracts` API is the **public contract boundary**
of the Electric Barometer ecosystem.

By using these entrypoints — and only these entrypoints —
you ensure that data entering EB is well-defined,
semantically correct, and safe to consume everywhere downstream.

If it isn’t validated here, it isn’t an EB artifact.
