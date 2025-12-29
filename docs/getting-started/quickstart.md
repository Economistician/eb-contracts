# Quickstart

This quickstart walks through a **minimal, end-to-end example**
of using **eb-contracts** to validate an Electric Barometer (EB) artifact.

The goal is not completeness, but confidence:
after this guide, you should understand how contracts fit into real workflows.

---

## Prerequisites

Before starting, ensure you have:

- Python 3.10 or newer
- `eb-contracts` installed
- Basic familiarity with pandas

If not installed yet, see `getting-started/install.md`.

---

## Step 1: Import validation entrypoints

All external consumers should use **stable validation entrypoints**.

```python
from eb_contracts import validate
from eb_contracts.validate import set_validation_mode
```

Avoid importing versioned contract classes directly (`v1`, `v2`);
they are implementation details.

---

## Step 2: Choose a validation mode

Set the validation behavior appropriate for your environment.

```python
set_validation_mode("strict")
```

Common choices:

- `"strict"` – CI pipelines, production ingestion
- `"warn"` – research notebooks
- `"off"` – trusted internal pipelines (use sparingly)

---

## Step 3: Create a simple forecast DataFrame

Create a minimal panel point forecast using pandas.

```python
import pandas as pd

df = pd.DataFrame(
    {
        "entity_id": ["A", "A", "B", "B"],
        "target_date": pd.to_datetime(
            ["2025-01-01", "2025-01-02", "2025-01-01", "2025-01-02"]
        ),
        "horizon": [1, 1, 1, 1],
        "prediction": [100.0, 110.0, 90.0, 95.0],
    }
)
```

This DataFrame is *not yet trusted*.
It becomes trustworthy only after validation.

---

## Step 4: Validate the forecast contract

Validate the DataFrame against a forecast contract.

```python
forecast = validate.panel_point_v1(df)
```

If validation succeeds:

- Schema is correct
- Semantics are interpretable
- The artifact is now contract-backed

If validation fails, an error or warning explains why.

---

## Step 5: Use the validated artifact downstream

Once validated, the artifact can be passed safely to:

- Evaluation pipelines
- Metric computation
- Optimization logic
- Applications

Downstream code should **assume correctness**
and avoid re-validating or reshaping.

---

## Optional: Attach run context

Add run-level metadata using a context contract.

```python
from eb_contracts.validate import run_context_v1

context = run_context_v1(
    run_id="example-run-001",
    environment="dev",
    pipeline="quickstart-demo",
)
```

Context travels alongside artifacts without altering data schemas.

---

## Common failure example

If required columns are missing or misnamed:

```python
bad_df = df.rename(columns={"prediction": "y_hat"})
validate.panel_point_v1(bad_df)
```

Validation will fail loudly, preventing silent errors downstream.

---

## What you gain by validating early

By validating at the boundary, you gain:

- Early failure instead of downstream bugs
- Explicit semantic guarantees
- Trust across system boundaries
- Reduced defensive programming

Contracts turn assumptions into code.

---

## Next steps

After completing this quickstart:

- Read `guides/forecasts.md` for forecast-specific details
- Read `guides/results.md` to understand evaluation artifacts
- Read `guides/costs.md` for asymmetric cost modeling
- Review `guides/interoperability.md` for ecosystem design

---

## Summary

This quickstart demonstrated the core EB workflow:

**Raw data → Contract validation → Trusted artifact → Downstream use**

Once this pattern is established, EB systems scale safely and predictably.

Validate early. Trust downstream.
