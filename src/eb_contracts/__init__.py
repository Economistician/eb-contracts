"""
Public API for EB contracts.

This package provides contract artifacts and validation entrypoints for
forecasting and panel-based evaluation.
"""

from __future__ import annotations

######################################
# Public API
######################################
from eb_contracts._runtime import set_validation_mode
from eb_contracts.validate import (
    panel_point_v1,
    panel_quantile_v1,
)

__all__ = [
    "panel_point_v1",
    "panel_quantile_v1",
    "set_validation_mode",
]
