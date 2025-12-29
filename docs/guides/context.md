# Run Context

This guide documents **run context contracts** in `eb-contracts`.

Run context captures **non-tabular, run-level metadata** that is essential for
reproducibility, auditability, and system-level reasoning across the
Electric Barometer (EB) ecosystem.

---

## What is run context?

A *run context* represents metadata about **how, when, and why** an EB artifact
was produced, rather than the data values themselves.

Examples include:

- Execution timestamps
- Environment identifiers (local, CI, production)
- Model or pipeline identifiers
- Scenario or experiment labels
- Free-form metadata needed for traceability

Run context is intentionally **separated from tabular artifacts**
(forecasts, costs, results) to avoid polluting data schemas with
operational concerns.

---

## Why context is a first-class contract

Electric Barometer emphasizes *decision accountability*.
That requires more than validated numbers — it requires provenance.

Run context enables:

- End-to-end traceability across pipelines
- Reproducible experiments and backtests
- Auditable production decisions
- Safe attachment of metadata without schema drift

By formalizing context as a contract, EB ensures that
metadata is **structured, explicit, and versioned**.

---

## The RunContextV1 contract

`RunContextV1` is the canonical container for run-level metadata.

Key characteristics:

- Explicit versioning (`v1`)
- Schema-validated fields
- Extensible metadata via controlled mappings
- Serializable and attachable to downstream artifacts

The contract defines *what context means*, not how it is stored or transported.

---

## Typical fields

While the exact fields are defined in code, typical run context values include:

- `run_id` – unique identifier for the execution
- `created_at` – timestamp of artifact creation
- `environment` – execution environment (e.g. dev, prod)
- `pipeline` – producing pipeline or system
- `model_id` – model or configuration identifier
- `notes` – optional human-readable annotations

Only fields defined by the contract are guaranteed to be stable.

---

## Attaching context to artifacts

Run context is designed to be **attached**, not embedded.

Common pattern:

1. Produce or ingest a tabular artifact
2. Validate it against its contract
3. Create a `RunContextV1`
4. Attach or associate context at the system boundary

Downstream consumers may rely on the presence of context,
but should not assume a specific storage mechanism.

---

## Validation behavior

Run context is validated just like tabular artifacts.

Validation ensures:

- Required fields are present
- Field types are correct
- Semantic constraints are respected

Validation mode (`strict`, `warn`, `off`) applies equally to context contracts,
allowing flexibility across environments.

---

## Versioning and evolution

Context contracts evolve cautiously.

Guidelines:

- Additive fields may be introduced in minor revisions
- Semantic changes require a new major version
- Deprecated fields are documented before removal

This ensures historical artifacts remain interpretable over time.

---

## Relationship to other contracts

Run context complements, but does not replace:

- Forecast contracts
- Cost contracts
- Result contracts

Those contracts define *what the data is*.
Context defines *how the data came to be*.

Together, they form a complete EB artifact boundary.

---

## Design principles

Run context follows these design principles:

- **Separation of concerns** – data vs metadata
- **Explicitness** – no hidden or ad-hoc fields
- **Versioned stability** – context is a contract, not a dict
- **Attachable** – context travels with artifacts without reshaping them

---

## When to extend context

If you find yourself adding operational columns to a DataFrame
(e.g. model name, run timestamp), that is usually a signal
that the information belongs in **run context**, not the data schema.

When in doubt, prefer context over columns.

---

## Summary

Run context provides the metadata backbone for Electric Barometer.

It ensures that every validated artifact can be understood,
reproduced, and audited — not just computed.

Treat context as infrastructure, not decoration.
