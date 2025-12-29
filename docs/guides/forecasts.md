# Forecast Contracts

This guide documents **forecast artifact contracts** in `eb-contracts`.

Forecast contracts define the **canonical shape, semantics, and validation rules**
for forecasts used throughout the Electric Barometer (EB) ecosystem.
They ensure that downstream systems can rely on forecasts without re-interpreting
structure or meaning.

---

## Why forecast contracts exist

Forecasts are foundational to Electric Barometer, but they are also fragile:

- Different teams encode horizons differently
- Entities and intervals are often implicit or overloaded
- Quantiles are inconsistently labeled or shaped
- Silent schema drift leads to incorrect evaluation and decisions

Forecast contracts eliminate ambiguity by making **forecast structure executable**.

If a forecast validates against an EB contract, its meaning is unambiguous.

---

## What a forecast contract represents

A forecast contract specifies:

- **What is being forecasted** (entities, intervals, horizons)
- **How predictions are represented** (point or quantile)
- **How rows relate to one another** (panel structure)
- **What semantic guarantees hold**

It does *not*:
- Train models
- Generate forecasts
- Define loss functions or decisions

Forecast contracts define *interfaces*, not implementations.

---

## Panel forecasts

Electric Barometer uses **panel-style forecasts**.

A panel forecast consists of observations indexed by:

- Entity (e.g. store, region, SKU)
- Time interval (e.g. day, week)
- Forecast horizon or target period

Each row represents a single forecasted value for a specific
entity–interval–horizon combination.

---

## Point vs quantile forecasts

EB distinguishes between two core forecast types.

---

### Panel point forecasts

A **panel point forecast** provides a single predicted value per row.

Use cases:
- Deterministic planning
- Baseline evaluation
- Downstream optimization that expects point estimates

Represented by:

- `PanelPointForecastV1`
- `PanelPointForecastV2` (where applicable)

---

### Panel quantile forecasts

A **panel quantile forecast** provides multiple predicted values
for different quantiles of the predictive distribution.

Use cases:
- Uncertainty-aware decision making
- Risk-sensitive evaluation
- Probabilistic readiness assessment

Represented by:

- `PanelQuantileForecastV1`
- `PanelQuantileForecastV2` (where applicable)

Quantile dimension is explicit and validated.

---

## Canonical columns and semantics

Forecast contracts enforce **canonical column names and meanings**.

While exact names are defined in code, they typically include:

- Entity identifiers
- Interval or target timestamps
- Horizon or lead information
- Prediction values
- Quantile identifiers (for quantile forecasts)

Canonical naming prevents downstream ambiguity and enables
consistent joins, aggregation, and evaluation.

---

## Validation behavior

Forecast contracts are validated on multiple dimensions:

- **Schema** – required columns and types
- **Shape** – panel structure consistency
- **Semantics** – interpretable horizons and quantiles
- **Numerics** – valid prediction values

Validation modes apply uniformly:

- **Strict** – violations raise errors
- **Warn** – violations emit warnings
- **Off** – validation is bypassed

This allows the same contract to be used across research and production.

---

## Versioning and evolution

Forecast contracts are explicitly versioned.

General guidance:

- Additive changes (new optional columns) may be introduced cautiously
- Semantic changes (e.g. horizon interpretation) require a new version
- Old versions remain supported for historical reproducibility

Consumers should rely on **stable validation entrypoints**
rather than importing versioned modules directly.

---

## Migration support

Where possible, migration utilities are provided to help upgrade
older forecast artifacts to newer contract versions.

Migration is:

- Explicit
- Opt-in
- Documented

Silent coercion is intentionally avoided.

---

## Relationship to results

Forecast contracts define *predictions*.
Result contracts define **aligned predictions and actuals**.

A typical flow:

1. Validate a forecast artifact
2. Join with realized actuals
3. Produce a result artifact
4. Evaluate or optimize using validated results

Each step has its own contract boundary.

---

## Common pitfalls avoided by contracts

Forecast contracts explicitly prevent:

- Mixing horizons with target timestamps incorrectly
- Treating quantile forecasts as point forecasts
- Implicit entity definitions
- Shape mismatches across panels

If a forecast validates, these errors cannot occur silently.

---

## Design principles

Forecast contracts follow these principles:

- **Explicit structure**
- **Panel-first design**
- **Semantic clarity**
- **Versioned stability**
- **Downstream safety**

---

## Summary

Forecast contracts are the structural backbone of Electric Barometer.

They ensure that every forecast entering the system has a clear,
validated meaning — enabling trustworthy evaluation, optimization,
and decision-making downstream.

Treat forecasts as contracts, not loose DataFrames.
