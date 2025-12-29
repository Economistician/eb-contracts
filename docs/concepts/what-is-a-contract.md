# What Is a Contract?

This document defines what a **contract** means in the context of
`eb-contracts` and the Electric Barometer (EB) ecosystem.

A contract is not a schema, a class, or a convenience wrapper.
It is a **semantic boundary with enforceable guarantees**.

---

## The problem contracts solve

In most data systems, meaning is implicit:

- Column names are suggestive, not guaranteed
- Validation is ad hoc or scattered
- Downstream systems defend themselves defensively
- Errors surface late, far from their source

As systems grow, this leads to:

- Silent semantic drift
- Incomparable historical results
- Fragile integrations
- Loss of trust in outputs

Electric Barometer introduces contracts to make **meaning explicit and enforceable**.

---

## Definition: contract

In EB, a **contract** is a versioned specification that defines:

- **Structure** – required fields, shapes, and types
- **Semantics** – what each field means
- **Units** – how numeric values are measured
- **Validation rules** – what is allowed or forbidden
- **Evolution guarantees** – how meaning changes over time

If an artifact satisfies a contract, its meaning is unambiguous.

---

## Contracts vs schemas

Schemas describe *shape*.
Contracts describe *meaning*.

A schema might say:
> “This column exists and is numeric.”

A contract says:
> “This column represents forecasted demand for a specific entity,
> target interval, and horizon, measured in counts.”

Schemas are necessary but insufficient.
Contracts subsume schemas.

---

## Contracts as boundaries

Contracts define **where responsibility changes hands**.

When an artifact crosses a contract boundary:

- The producer guarantees correctness
- The consumer assumes correctness
- Validation happens once, at the boundary

This eliminates duplicated checks and defensive programming downstream.

---

## Contracts are executable documentation

Contracts are not prose descriptions.
They are **executable specifications**.

Validation code:

- Encodes the rules
- Enforces the guarantees
- Produces precise failure signals

Documentation explains *why*;
contracts enforce *what*.

---

## Contracts are versioned promises

A contract version is a promise that:

- Validated artifacts remain interpretable
- Semantic meaning does not change silently
- Historical results remain comparable

If meaning changes, the version must change.

Versioning protects trust over time.

---

## Contracts vs configuration

Contracts are not configuration knobs.

They do not:

- Tune behavior dynamically
- Encode business rules directly
- Change based on environment

Contracts define **what data is**, not **how it is used**.

---

## Types of contracts in EB

Electric Barometer uses multiple contract families:

- **Forecast contracts** – predictions and uncertainty
- **Cost contracts** – asymmetric penalties and economics
- **Result contracts** – aligned predictions and actuals
- **Context contracts** – run-level metadata

Each family defines a distinct semantic boundary.

---

## Validation modes do not weaken contracts

Validation modes control **enforcement behavior**, not contract meaning.

Even when validation is disabled:

- The contract still defines meaning
- Semantic guarantees still exist
- Violations are still violations

Contracts are authoritative regardless of enforcement mode.

---

## Contracts and interoperability

Contracts enable interoperability by:

- Eliminating implicit assumptions
- Providing shared vocabulary
- Enforcing consistent interpretation

Two systems that agree on a contract version can interoperate safely
without sharing implementation details.

---

## Contracts and failure

Contracts are designed to **fail loudly**.

Failure means:

- Meaning cannot be guaranteed
- The artifact must not proceed
- Responsibility is clear

A failing contract is safer than a silently corrupted artifact.

---

## Common misconceptions

Contracts are **not**:

- Just data classes
- Just schemas
- Just validation utilities
- Optional documentation

They are the foundation of EB’s reliability model.

---

## Design principles

Contracts in EB follow these principles:

- **Meaning before structure**
- **Explicit over implicit**
- **Fail early, fail clearly**
- **Versioned guarantees**
- **Boundary-based responsibility**

---

## Summary

A contract is Electric Barometer’s unit of trust.

It defines meaning, enforces correctness, and preserves comparability over time.
Without contracts, EB would be a collection of scripts.
With contracts, it is a system.

Treat contracts as infrastructure — because they are.
