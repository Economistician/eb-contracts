# Electric Barometer · Contracts (`eb-contracts`)

![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)

Data contract and validation layer for the Electric Barometer ecosystem, defining canonical schemas, semantics, and enforcement for forecasts, costs, results, and run context.

---

## Overview

`eb-contracts` defines versioned schemas and validators for demand panels, forecasts, costs, and run context. It enforces shared structure and semantics; it does not compute metrics or train models.

---

## Installation

`eb-contracts` is distributed as a standard Python package.

```bash
pip install eb-contracts
```

---

## Core Concepts

- **Canonical data contracts** — Core data artifacts (forecasts, cost specifications, results, and context) are represented using explicit, versioned schemas rather than implicit conventions or ad-hoc DataFrame shapes.

- **Semantic consistency** — Column names, units, grain, and meaning are standardized and enforced so that downstream systems can rely on shared interpretation rather than contextual knowledge or undocumented assumptions.

- **Validation as a boundary** — Contract validation establishes a clear boundary between “valid” and “invalid” data, preventing silent failures and making structural issues visible at ingestion time rather than during downstream computation.

- **Versioned evolution** — Contracts are versioned to allow schemas and semantics to evolve over time without breaking existing consumers, enabling forward progress while preserving backward compatibility.

- **Explicit migration** — Adaptation from external or legacy data formats into contract-compliant artifacts is performed through explicit migration utilities, avoiding implicit coercion or guesswork.

- **Separation of structure from logic** — Data shape and meaning are defined independently of metric computation, optimization, or execution logic, ensuring that structural correctness is not entangled with algorithmic behavior.

---

## Minimal Example

The example below illustrates a typical contract workflow using `eb-contracts`: adapting an external forecast frame into a canonical contract artifact and validating it at the system boundary.

```python
import pandas as pd

from eb_contracts import set_validation_mode
from eb_contracts.api import PanelPointColumns, to_panel_point_v1

raw = pd.DataFrame(
    {
        "store": ["A", "A"],
        "timestamp": [
            pd.Timestamp("2025-01-01 00:00:00"),
            pd.Timestamp("2025-01-01 00:30:00"),
        ],
        "actual": [10.0, 12.0],
        "forecast": [11.0, 13.0],
    }
)

columns = PanelPointColumns(
    entity_id="store",
    interval_start="timestamp",
    y_true="actual",
    y_pred="forecast",
)

with set_validation_mode("strict"):
    forecast = to_panel_point_v1(raw, columns=columns)

print(type(forecast))
```

---

## License

BSD 3-Clause License.
© 2026 Kyle Corrie.
