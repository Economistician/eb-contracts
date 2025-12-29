"""
Public validation entrypoints for contract artifacts.

This module defines stable, versioned entrypoints for validating and constructing
contract-wrapped data artifacts. Consumers should prefer these functions over
importing versioned contract modules directly.
"""

from __future__ import annotations

import pandas as pd

from eb_contracts.costs.v1 import (
    CostAsymmetrySpecV1,
)
from eb_contracts.forecast.v1 import (
    PanelPointForecastV1,
    PanelQuantileForecastV1,
)
from eb_contracts.results.v1 import (
    PanelPointResultV1,
)

######################################
# Public API
######################################


def panel_point_v1(frame: pd.DataFrame) -> PanelPointForecastV1:
    """Validate and construct a V1 panel point forecast artifact."""
    return PanelPointForecastV1.from_frame(frame)


def panel_quantile_v1(frame: pd.DataFrame) -> PanelQuantileForecastV1:
    """Validate and construct a V1 panel quantile forecast artifact."""
    return PanelQuantileForecastV1.from_frame(frame)


def cost_asymmetry_v1(frame: pd.DataFrame) -> CostAsymmetrySpecV1:
    """Validate and construct a V1 cost-asymmetry specification artifact."""
    return CostAsymmetrySpecV1.from_frame(frame)


def panel_point_result_v1(frame: pd.DataFrame) -> PanelPointResultV1:
    """Validate and construct a V1 panel point result artifact."""
    return PanelPointResultV1.from_frame(frame)
