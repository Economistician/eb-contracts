# Installation

This guide describes how to install **eb-contracts** and prepare your environment
to use Electric Barometer (EB) data contracts safely and consistently.

---

## Requirements

`eb-contracts` is designed as lightweight, foundational infrastructure.

Minimum requirements:

- **Python**: 3.10 or newer
- **Operating systems**: Linux, macOS, Windows
- **Core dependency**: pandas

The library has no optional runtime services, databases, or external systems.

---

## Installing from PyPI

The recommended installation method is via **pip**:

```bash
pip install eb-contracts
```

This installs:

- Contract definitions
- Validation runtime
- Migration utilities
- Canonical column and semantic definitions

---

## Installing in a virtual environment (recommended)

For isolation and reproducibility, use a virtual environment.

Example using `venv`:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install eb-contracts
```

This ensures contract behavior is consistent across projects.

---

## Installing alongside other EB packages

`eb-contracts` is intended to be shared across the EB ecosystem.

Common combinations:

```bash
pip install eb-contracts eb-metrics eb-evaluation eb-optimization
```

Contracts should be installed **once per environment** and reused
by all downstream EB components.

---

## Version pinning (recommended)

Because contracts define **interfaces**, version pinning is strongly encouraged
in production and research pipelines.

Example:

```text
eb-contracts==1.*
```

This allows patch-level fixes while protecting against breaking changes.

---

## Verifying installation

After installation, verify that the package imports correctly:

```python
import eb_contracts
```

You can also inspect the public validation entrypoints:

```python
from eb_contracts import validate
```

If imports succeed, installation is complete.

---

## First validation check

A minimal sanity check:

```python
from eb_contracts.validate import set_validation_mode

set_validation_mode("strict")
```

If no error is raised, the validation runtime is active.

---

## No additional setup required

`eb-contracts` requires:

- No configuration files
- No environment variables
- No service initialization

Validation behavior is controlled programmatically.

---

## Upgrading

To upgrade within a major version:

```bash
pip install --upgrade eb-contracts
```

Before upgrading across major versions, review:

- `docs/changelog.md`
- Migration guides
- Version compatibility notes

---

## Troubleshooting

If installation fails:

1. Confirm Python version compatibility
2. Ensure pip is up to date
3. Check for conflicting pinned dependencies

Because `eb-contracts` has minimal dependencies,
installation issues are usually environment-related.

---

## Summary

Installing `eb-contracts` gives your environment a **canonical contract layer**
for Electric Barometer.

Once installed, all EB components can rely on shared,
validated definitions of forecasts, costs, results, and context.

Install once. Validate everywhere.
