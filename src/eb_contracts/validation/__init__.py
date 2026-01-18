"""
Validation primitives for EB contracts.

This subpackage defines structured validation errors and violation artifacts
produced when contract validation fails or detects non-conformant data.

These types are part of the public contracts API and may be imported by callers
to inspect, handle, or surface validation outcomes.
"""

from __future__ import annotations

from .errors import ContractViolation, ContractViolationError

__all__ = [
    "ContractViolation",
    "ContractViolationError",
]
