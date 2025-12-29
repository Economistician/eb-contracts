from __future__ import annotations

import pandas as pd
import pytest

from eb_contracts._errors import ContractViolationError
from eb_contracts._runtime import set_validation_mode
from eb_contracts.definitions.conventions import (
    ENTITY_ID,
    INTERVAL_START,
    Y_PRED,
    Y_PRED_Q,
    Y_TRUE,
    Q,
)
from eb_contracts.forecast.v1 import (
    PanelPointForecastV1,
    PanelQuantileForecastV1,
)
from eb_contracts.validate import (
    panel_point_v1,
    panel_quantile_v1,
)

######################################
# Helpers
######################################


def _panel_point_minimal(*, duplicate: bool = False) -> pd.DataFrame:
    ts = [
        pd.Timestamp("2025-01-01 00:00:00"),
        pd.Timestamp("2025-01-01 00:30:00"),
    ]
    if duplicate:
        ts = [ts[0], ts[0]]

    return pd.DataFrame(
        {
            ENTITY_ID: ["A", "A"],
            INTERVAL_START: ts,
            Y_TRUE: [10.0, 12.0],
            Y_PRED: [11.0, 13.0],
        }
    )


def _panel_quantile_minimal(*, q_out_of_range: bool = False) -> pd.DataFrame:
    q = [0.5, 0.9]
    if q_out_of_range:
        q = [0.5, 1.0]

    return pd.DataFrame(
        {
            ENTITY_ID: ["A", "A"],
            INTERVAL_START: [
                pd.Timestamp("2025-01-01 00:00:00"),
                pd.Timestamp("2025-01-01 00:00:00"),
            ],
            Y_TRUE: [10.0, 10.0],
            Q: q,
            Y_PRED_Q: [9.0, 12.0],
        }
    )


######################################
# Entry points: strict mode
######################################


def test_panel_point_v1_returns_point_artifact() -> None:
    df = _panel_point_minimal()
    with set_validation_mode("strict"):
        artifact = panel_point_v1(df)
    assert isinstance(artifact, PanelPointForecastV1)
    assert artifact.frame is df


def test_panel_quantile_v1_returns_quantile_artifact() -> None:
    df = _panel_quantile_minimal()
    with set_validation_mode("strict"):
        artifact = panel_quantile_v1(df)
    assert isinstance(artifact, PanelQuantileForecastV1)
    assert artifact.frame is df


def test_panel_point_v1_strict_raises_on_invalid_frame() -> None:
    df = _panel_point_minimal(duplicate=True)
    with set_validation_mode("strict"), pytest.raises(ContractViolationError):
        panel_point_v1(df)


def test_panel_quantile_v1_strict_raises_on_invalid_frame() -> None:
    df = _panel_quantile_minimal(q_out_of_range=True)
    with set_validation_mode("strict"), pytest.raises(ContractViolationError):
        panel_quantile_v1(df)


######################################
# Entry points: warn / off modes
######################################


def test_panel_point_v1_warn_does_not_raise() -> None:
    df = _panel_point_minimal(duplicate=True)
    with set_validation_mode("warn"):
        panel_point_v1(df)


def test_panel_point_v1_off_does_not_raise() -> None:
    df = _panel_point_minimal(duplicate=True)
    with set_validation_mode("off"):
        panel_point_v1(df)


def test_panel_quantile_v1_warn_does_not_raise() -> None:
    df = _panel_quantile_minimal(q_out_of_range=True)
    with set_validation_mode("warn"):
        panel_quantile_v1(df)


def test_panel_quantile_v1_off_does_not_raise() -> None:
    df = _panel_quantile_minimal(q_out_of_range=True)
    with set_validation_mode("off"):
        panel_quantile_v1(df)
