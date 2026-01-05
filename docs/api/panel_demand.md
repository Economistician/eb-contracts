# PanelDemandV1 — Demand Panel Contract

PanelDemandV1 defines a **generic, governance-aware contract** for representing demand or usage data in a form suitable for:

- forecasting
- Demand Quantization Compatibility (DQC)
- Forecastability & Policy Contracts (FPC)
- cost-aware evaluation and optimization

This contract is **domain-agnostic**. It does not assume any specific industry, unit, or cadence.
Domain-specific datasets are expected to conform to this contract via **adapters**, not by modifying the contract itself.

---

## Design Principles

PanelDemandV1 is intentionally:

- **Panel-based** — multiple demand series observed over time
- **Scaffold-tolerant** — rows may exist even when demand is impossible or unobservable
- **Gate-driven** — admissibility is encoded via explicit boolean signals
- **Evaluation-safe** — prevents invalid scoring, leakage, and misinterpretation
- **Composable** — designed to interoperate with DQC, FPC, RAL, and optimization layers

The contract defines **what demand means**, not how it should be modeled.

---

## Conceptual Model

Each row represents a potential observation of demand for a specific entity at a specific time.

Crucially:
- **Row existence does not imply demand was possible**
- **NULL does not imply zero**
- **Forecast suppression is a valid and expected outcome**

Meaning is carried by **gates**, not by presence or absence of rows.

---

## Required Roles

A dataset conforms to PanelDemandV1 if it can supply the following roles.

### 1. Identity (Keys)

One or more columns that uniquely identify a demand series.

Examples:
- store × commodity
- region × product
- queue × call type
- unit × patient class

Requirements:
- Keys must be stable over time
- Time ordering is evaluated *within* each key group

---

### 2. Time Index (Choose One Mode)

PanelDemandV1 supports two mutually exclusive time representations.

#### Mode A — Timestamp-based

- `ts` : datetime
  - Must be monotonic within each key
  - May be timezone-aware or local-naive, but must be consistent

Use this mode when demand is observed at irregular or continuous times.

---

#### Mode B — Day + Interval Index

- `day` : date-like (calendar or business day)
- `interval_index` : integer
  - Zero-based
  - Ranges from `0` to `periods_per_day - 1`

Required metadata:
- `interval_minutes` : int (e.g., 30)
- `periods_per_day` : int (e.g., 48)

Optional metadata:
- `business_day_start_local_minutes`
  - Used when operational days do not align with calendar days
  - Example: `240` for a 4:00 AM → 4:00 AM business day

Use this mode for intraday operational forecasting.

---

### 3. Target (Demand)

- `y` : numeric, nullable

Represents realized demand or usage during the time bucket.

Rules:
- `y >= 0` whenever present
- Units are domain-defined (counts, weight, volume, etc.)
- NULL is permitted and semantically meaningful

PanelDemandV1 does **not** assume:
- integer demand
- continuous demand
- Poisson-like behavior

Those properties are diagnosed separately (e.g., via DQC).

---

### 4. Governance Gates

All gates must be boolean (or castable to boolean).

#### `is_observable`
Indicates whether the time interval is observable and scorable.

Examples:
- store open window
- valid telemetry window
- system online

If `False`, the row must not be scored.

---

#### `is_possible`
Indicates whether demand is *possible* during this interval.

Examples:
- item offered for sale
- service available
- queue open

If `False`, realized demand is not expected.

---

#### `is_structural_zero`
Indicates that demand is **impossible by design**.

Examples:
- item not stocked
- service permanently unavailable
- structural exclusion

This must be `True` only when demand cannot occur under any circumstance.

---

### Canonical Admissible Slice

For evaluation, diagnostics, and DQC, the canonical admissible slice is:

admissible =
    is_observable
    AND is_possible
    AND NOT is_structural_zero

Rows outside this slice must not be scored or used to infer demand structure.

---

## Null Semantics

PanelDemandV1 explicitly distinguishes:

- NULL demand (no realized usage)
- zero demand (realized but zero)
- structurally impossible demand

The meaning of NULL is domain-specific and must be governed by gates.

Implementations may optionally declare a policy such as:
- "y must be present on all admissible rows"
- or "y may be NULL on admissible rows"

---

## Adapter Pattern (Required)

PanelDemandV1 is **not tied to column names**.

Domain datasets must be adapted into the contract via an adapter that:
- maps domain columns to contract roles
- emits a normalized DataFrame with canonical column names
- supplies required metadata

Adapters are expected to live outside the core EB ecosystem.

---

## Relationship to Other EB Components

- **DQC** consumes PanelDemandV1 to diagnose demand support structure
- **FPC / RAL** operate only on admissible slices defined here
- **Optimization** relies on the same gates to ensure fair evaluation
- **Forecast artifacts** (point, quantile) are evaluated *against* PanelDemandV1

PanelDemandV1 must be validated **before** any downstream component is applied.

---

## What This Contract Does Not Do

PanelDemandV1 does not:
- define forecasting models
- define cost functions
- measure accuracy
- infer demand structure
- optimize parameters

Its sole purpose is to ensure **semantic correctness and governance safety**.

---

## Versioning

This document defines **PanelDemandV1**.

Future versions may:
- add additional gate roles
- support alternative time semantics
- introduce stricter validation modes

Backward compatibility will be preserved through explicit versioning.

---

## Summary

PanelDemandV1 provides a **minimal, explicit, and auditable foundation** for demand forecasting ecosystems.

If a dataset conforms to PanelDemandV1, it can be safely:
- diagnosed (DQC)
- evaluated (FPC / cost-aware metrics)
- optimized
- compared across models and domains

If it does not, downstream results are not trustworthy.

This contract exists to prevent that failure mode.
