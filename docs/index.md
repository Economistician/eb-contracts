# eb-contracts

Canonical data contracts for the **Electric Barometer (EB)** ecosystem.

---

## What is eb-contracts?

`eb-contracts` defines **stable, versioned data contracts** for Electric Barometer artifacts.
A *contract* specifies:

- **Canonical schemas** (required columns, types, shapes)
- **Semantic meaning** (what each field represents)
- **Validation rules** (what is allowed, warned, or rejected)
- **Version boundaries** (what changes are breaking vs additive)

The purpose of this repository is to ensure that *all downstream EB components*
— metrics, evaluation, optimization, adapters, and applications — operate on
**well-defined, trustworthy data shapes**.

If an artifact validates against an EB contract, it is safe to consume anywhere
in the EB ecosystem.

---

## What eb-contracts is NOT

It is important to be explicit about boundaries.

`eb-contracts` does **not**:

- Perform forecasting or modeling
- Compute metrics or loss functions
- Optimize decisions or policies
- Transform raw source data end-to-end

Those responsibilities live in other repositories (e.g. adapters, metrics,
evaluation, optimization).
This repo exists purely to define and enforce *interfaces* between them.

---

## Why contracts matter in Electric Barometer

Electric Barometer emphasizes **cost-aware, asymmetric decision-making**.
That requires more than numeric correctness — it requires *semantic correctness*.

Contracts ensure that:

- Forecasts align to the correct **entities, intervals, and horizons**
- Cost asymmetry specifications are **explicit and interpretable**
- Results align predictions and actuals without silent leakage or drift
- Run-level metadata is preserved and auditable
- Schema drift is detected early, not after metrics or optimization fail

In short: contracts turn *data assumptions* into *executable guarantees*.

---

## Contract families

The repository currently defines contracts for:

- **Forecast artifacts**
  - Panel point forecasts
  - Panel quantile forecasts
- **Cost specifications**
  - Cost asymmetry parameters
- **Result artifacts**
  - Aligned predictions and actuals
- **Run context**
  - Execution- and run-level metadata

Each family is versioned independently and exposed through stable validation
entrypoints.

---

## Versioning model

All contracts are **explicitly versioned** (e.g. `v1`, `v2`).

General rules:

- Versioned modules define the *schema and validation logic*
- Public consumers should use **stable entrypoints** in `eb_contracts.validate`
- Breaking schema or semantic changes require a new major version
- Additive, backward-compatible changes may be introduced within a version

Migration helpers are provided where appropriate to support safe transitions.

---

## Validation philosophy

Validation is a *first-class operation*.

Artifacts can be validated in different modes:

- **Strict** – violations raise errors
- **Warn** – violations emit warnings but allow execution
- **Off** – validation is bypassed

This allows the same contracts to be used across:

- CI pipelines
- Production ingestion
- Research notebooks
- Exploratory analysis

Without duplicating logic or weakening guarantees.

---

## Typical usage

A common pattern across the EB ecosystem:

1. Raw data is produced or adapted upstream
2. The artifact is validated against an EB contract
3. A validated, contract-wrapped object is passed downstream
4. All consumers rely on the contract guarantees, not ad-hoc checks

This sharply reduces defensive programming and hidden assumptions.

---

## Relationship to the EB ecosystem

`eb-contracts` sits at the **core boundary layer** of Electric Barometer:

- **Adapters** map raw sources → canonical contracts
- **Metrics & evaluation** assume validated contracts
- **Optimization & policies** operate on contract-backed artifacts
- **Applications** trust contracts as stable interfaces

If a component accepts an EB contract, it should not need to re-validate
the underlying data shape.

---

## Getting started

- See **Getting Started** for installation and a quick validation example
- See **Concepts** for contract philosophy and semantics
- See **Guides** for artifact-specific usage
- See **API Reference** for constructors and validators

---

## Design principles

This repository follows a few core principles:

- **Explicit over implicit**
- **Semantics over convenience**
- **Versioned over mutable**
- **Fail early, fail clearly**
- **One canonical truth per artifact type**

These principles are enforced not by convention, but by code.

---

## Status

`eb-contracts` is actively developed and considered foundational infrastructure
for the Electric Barometer ecosystem.

Contract stability and backward compatibility are treated as high-priority
concerns.
