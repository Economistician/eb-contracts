# Versioning

This document defines the **versioning model** used in `eb-contracts`.

Versioning in Electric Barometer (EB) is not about release cadence or marketing.
It is about **preserving semantic meaning, historical validity, and system trust**
as contracts evolve over time.

---

## Why versioning is critical

Contracts define meaning.

If contract meaning changes without versioning:

- Historical artifacts become ambiguous
- Metrics and decisions lose comparability
- Reproducibility is compromised
- Trust in the system erodes

EB treats versioning as a **semantic safety mechanism**, not a convenience.

---

## What is versioned

In `eb-contracts`, the following are versioned together:

- Schemas (required columns, shapes)
- Canonical column names
- Semantic meaning of fields
- Validation rules and guarantees
- Interpretability assumptions

If any of these change materially, the version must change.

---

## Version scope

Contracts are versioned **by artifact family**, not globally.

Examples:
- Forecast contracts (`PanelPointForecastV1`, `V2`, …)
- Cost contracts (`CostAsymmetrySpecV1`, …)
- Result contracts (`PanelPointResultV1`, …)
- Context contracts (`RunContextV1`, …)

Each family evolves independently.

---

## Major versions

A **major version** change (e.g. `v1` → `v2`) indicates a **semantic change**.

Major versions are required when:

- Column meaning changes
- Alignment semantics change
- Validation rules tighten materially
- Downstream interpretation would change

Major versions are intentionally rare and explicit.

---

## Minor and patch changes

Within a major version:

- **Patch changes** may fix bugs without affecting semantics
- **Additive changes** may introduce optional fields cautiously
- Validation behavior must remain compatible

If a consumer relying on `v1` semantics would interpret data differently,
the change is not allowed without a new major version.

---

## Stable entrypoints

External consumers should **never import versioned modules directly**.

Instead, they should use **stable entrypoints** exposed via:

```python
from eb_contracts import validate
```

Stable entrypoints:

- Route to the correct version internally
- Allow internal refactoring
- Protect consumers from structural churn

Versioned modules are implementation details.

---

## Backward compatibility guarantees

For an active major version:

- Required columns will not be removed
- Column semantics will not change
- Validation rules will not silently tighten
- Historical artifacts remain interpretable

Backward compatibility is treated as a product guarantee.

---

## Deprecation policy

When a contract version is slated for replacement:

- It is documented in the changelog
- Migration guidance is provided where possible
- Deprecation periods are explicit

Deprecated versions remain readable for historical analysis.

---

## Migration and versioning

Versioning and migration are coupled but distinct.

- Versioning defines *what changed*
- Migration defines *how to move forward safely*

Migration is never implicit and never automatic.

---

## When NOT to version

Do **not** create a new version for:

- Documentation clarifications
- Internal refactors with no semantic impact
- Performance improvements
- Error message wording

Version numbers are reserved for meaning changes.

---

## Common anti-patterns

Avoid:

- Renaming columns without versioning
- Tightening validation rules silently
- Adding required fields mid-version
- Treating versions as interchangeable

These patterns undermine contract trust.

---

## Design principles

EB versioning follows these principles:

- **Semantic stability over convenience**
- **Explicit change signaling**
- **Backward compatibility by default**
- **Versioned meaning, not code**
- **Historical reproducibility**

---

## Summary

Versioning is how Electric Barometer protects meaning over time.

A version number is a promise:
that validated artifacts will remain interpretable,
comparable, and trustworthy — now and in the future.

If meaning changes, the version must change.
