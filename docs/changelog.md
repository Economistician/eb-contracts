# Changelog

All notable changes to **eb-contracts** are documented in this file.

This project follows a **contract-first versioning philosophy**:
schema and semantic stability are treated as critical infrastructure concerns.
Breaking changes are explicit, versioned, and deliberate.

---

## Versioning policy

Contracts are versioned independently by artifact family (e.g. forecasts, costs).
Each contract version guarantees:

- Stable required columns and shapes
- Stable semantic meaning of fields
- Stable validation behavior under the same mode

Changes fall into three categories:

- **Added** – backward-compatible additions
- **Changed** – semantic or behavioral changes
- **Deprecated / Removed** – breaking changes (require new major version)

Public consumers should always prefer **stable entrypoints**
exposed via `eb_contracts.validate`.

---

## [Unreleased]

### Added
- Centralized validation entrypoints in `eb_contracts.validate`
- Validation runtime with configurable modes (`strict`, `warn`, `off`)
- Canonical column definitions and semantic descriptors
- Migration utilities for forecast artifacts

### Changed
- None

### Deprecated
- None

---

## [v1.0.0] – Initial public contract release

### Added

#### Forecast contracts
- `PanelPointForecastV1`
  - Canonical schema for panel-style point forecasts
  - Required entity, interval, horizon, and prediction columns
- `PanelQuantileForecastV1`
  - Canonical schema for panel-style quantile forecasts
  - Explicit quantile dimension enforcement

#### Cost contracts
- `CostAsymmetrySpecV1`
  - Explicit cost ratio specification for asymmetric error evaluation
  - Validation of cost positivity and interpretability

#### Result contracts
- `PanelPointResultV1`
  - Aligned actuals and predictions for evaluation
  - Enforced temporal and entity consistency

#### Context contracts
- `RunContextV1`
  - Run-level metadata container for EB executions
  - Stable attachment mechanism for non-tabular metadata

#### Definitions & semantics
- Canonical column naming conventions
- Semantic descriptors for measures and identifiers
- Unit annotations for numeric fields

#### Validation & runtime
- Contract-aware validation engine
- Structured error and warning reporting
- Validation mode control for CI vs exploratory workflows

---

## Migration support

### Forecast artifact migration
- Column mapping helpers for panel forecast schemas
- Safe upgrade paths between contract versions where applicable

Migration utilities are intentionally explicit and opt-in to prevent
silent semantic drift.

---

## Stability guarantees

For all `v1` contracts:

- No required column removals
- No semantic reinterpretation of existing fields
- No tightening of validation rules without version bump

Bug fixes that do not affect schema or semantics may be released as patch updates.

---

## How to read this changelog

- **Added** entries describe new contracts or capabilities
- **Changed** entries describe semantic or behavioral shifts
- **Deprecated / Removed** entries indicate breaking changes
- If an entry affects downstream consumers, it will be called out explicitly

---

## Commitment to compatibility

`eb-contracts` is foundational infrastructure for the Electric Barometer ecosystem.
Backward compatibility is treated as a product feature, not an afterthought.

Breaking changes are rare, intentional, and documented.
