# Interoperability

This guide explains how **eb-contracts** enables safe, scalable interoperability
across the Electric Barometer (EB) ecosystem.

Interoperability is not achieved by loose conventions, but by **explicit,
validated contract boundaries** between systems.

---

## What interoperability means in EB

In Electric Barometer, interoperability means:

- Components can exchange artifacts without renegotiating meaning
- Data produced by one system can be safely consumed by another
- Semantic assumptions are enforced, not implied
- Failures occur early, clearly, and at boundaries

Contracts are the mechanism that makes this possible.

---

## The contract boundary model

EB is organized around **contract boundaries**, not shared implementations.

Each major layer:

- Adapters
- Contracts
- Metrics & evaluation
- Optimization & policies
- Applications

Communicates using **validated artifacts**, not raw DataFrames or ad-hoc objects.

`eb-contracts` defines those artifacts.

---

## Role of eb-contracts

`eb-contracts` acts as the **canonical interface layer** of the ecosystem.

It provides:

- Stable schemas for shared artifacts
- Explicit semantic definitions
- Versioned evolution paths
- Validation as executable documentation

If two components agree on a contract version, they can interoperate safely.

---

## Relationship to adapters

Adapters are responsible for:

- Ingesting raw, source-specific data
- Mapping source schemas to EB canonical schemas
- Producing contract-valid artifacts

Adapters should *always* validate outputs against `eb-contracts`
before emitting artifacts downstream.

Contracts absorb variability; adapters isolate it.

---

## Relationship to metrics and evaluation

Metrics and evaluation components:

- Assume artifacts are already validated
- Rely on contract semantics (e.g. horizon meaning, cost direction)
- Should not re-interpret or reshape data

This allows metrics to remain focused on computation,
not defensive data handling.

---

## Relationship to optimization and policies

Optimization layers consume:

- Forecast contracts
- Cost contracts
- Result contracts
- Run context

They depend on contracts to ensure:

- Objective functions are well-defined
- Costs are interpretable
- Decisions are auditable

Optimization logic should never depend on raw schema details
outside the contract definition.

---

## Relationship to applications

Applications (dashboards, tools, APIs):

- Consume validated EB artifacts
- May enrich artifacts with presentation-layer metadata
- Should not mutate contract semantics

Contracts enable applications to evolve independently
from upstream data producers.

---

## Stable entrypoints vs internal versions

Interoperability depends on **stable entrypoints**.

Rules:

- External consumers use `eb_contracts.validate.*`
- Versioned modules (`v1`, `v2`) are internal implementation details
- Direct imports of versioned contracts by consumers are discouraged

This allows contracts to evolve without breaking consumers.

---

## Version compatibility expectations

Interoperability requires shared expectations:

- Producers and consumers must agree on contract versions
- Older versions remain supported for historical artifacts
- New versions require explicit adoption

Silent coercion between versions is intentionally avoided.

---

## Failure modes and guarantees

Contracts define *where* failures occur.

With contracts:

- Schema violations fail at validation time
- Semantic mismatches are detected early
- Downstream systems can assume correctness

Without contracts:

- Failures are delayed
- Errors are harder to diagnose
- Responsibility is unclear

Interoperability is as much about **failure clarity**
as it is about success.

---

## Extending the ecosystem safely

When adding a new component:

1. Identify which EB contracts it consumes
2. Validate inputs at the boundary
3. Emit only contract-valid artifacts
4. Avoid leaking internal representations

This keeps the ecosystem modular and evolvable.

---

## Design principles

Interoperability in EB is guided by:

- **Explicit contracts over implicit conventions**
- **Validation at boundaries**
- **Versioned stability**
- **Separation of concerns**
- **Semantic integrity**

---

## Summary

`eb-contracts` is the interoperability backbone of Electric Barometer.

By enforcing explicit, versioned contracts at system boundaries,
it allows independent components to evolve while remaining compatible.

Interoperability is not accidental — it is designed.
