"""
PanelDemandV1 contract.

A domain-agnostic, governance-aware demand panel contract intended to support forecasting,
DQC, FPC/RAL diagnostics, and cost-aware evaluation.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

import pandas as pd

TimeMode = Literal["timestamp", "day_interval"]


@dataclass(frozen=True, slots=True)
class PanelDemandV1:
    """A normalized, validated demand panel."""

    frame: pd.DataFrame
    keys: tuple[str, ...]
    y_col: str

    time_mode: TimeMode
    ts_col: str | None = None
    day_col: str | None = None
    interval_index_col: str | None = None

    interval_minutes: int | None = None
    periods_per_day: int | None = None
    business_day_start_local_minutes: int | None = None

    is_observable_col: str = "is_observable"
    is_possible_col: str = "is_possible"
    is_structural_zero_col: str = "is_structural_zero"

    @classmethod
    def from_frame(
        cls,
        frame: pd.DataFrame,
        *,
        keys: Sequence[str],
        y_col: str,
        time_mode: TimeMode,
        ts_col: str | None = None,
        day_col: str | None = None,
        interval_index_col: str | None = None,
        interval_minutes: int | None = None,
        periods_per_day: int | None = None,
        business_day_start_local_minutes: int | None = None,
        is_observable_col: str = "is_observable",
        is_possible_col: str = "is_possible",
        is_structural_zero_col: str = "is_structural_zero",
        validate: bool = True,
    ) -> PanelDemandV1:
        obj = cls(
            frame=frame,
            keys=tuple(keys),
            y_col=y_col,
            time_mode=time_mode,
            ts_col=ts_col,
            day_col=day_col,
            interval_index_col=interval_index_col,
            interval_minutes=interval_minutes,
            periods_per_day=periods_per_day,
            business_day_start_local_minutes=business_day_start_local_minutes,
            is_observable_col=is_observable_col,
            is_possible_col=is_possible_col,
            is_structural_zero_col=is_structural_zero_col,
        )
        if validate:
            validate_panel_demand_v1(obj)
        return obj


def validate_panel_demand_v1(panel: PanelDemandV1) -> None:
    """Validate a PanelDemandV1 instance.

    Validation is semantic (governance-aware) and designed to prevent misuse:
    - Keys and time index must exist
    - Gates must exist and be boolean/castable-to-bool
    - y must be numeric when present and nonnegative
    - time must be well-formed per mode

    Notes:
    - We intentionally keep this validator minimal and deterministic.
    - Monotonicity checks may be added later (or made configurable) to avoid
      over-constraining datasets that rely on scaffolds or sparse windows.
    """
    df = panel.frame

    # --- required columns
    required: list[str] = [
        *panel.keys,
        panel.y_col,
        panel.is_observable_col,
        panel.is_possible_col,
        panel.is_structural_zero_col,
    ]

    if panel.time_mode == "timestamp":
        if not panel.ts_col:
            raise ValueError("time_mode='timestamp' requires ts_col.")
        required.append(panel.ts_col)

    elif panel.time_mode == "day_interval":
        if not panel.day_col or not panel.interval_index_col:
            raise ValueError("time_mode='day_interval' requires day_col and interval_index_col.")
        required.extend([panel.day_col, panel.interval_index_col])

        if panel.interval_minutes is None or panel.periods_per_day is None:
            raise ValueError(
                "time_mode='day_interval' requires interval_minutes and periods_per_day."
            )

    else:
        raise ValueError(f"Unrecognized time_mode: {panel.time_mode!r}")

    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # --- gates: boolean / castable-to-bool
    for gate_col in (panel.is_observable_col, panel.is_possible_col, panel.is_structural_zero_col):
        s = df[gate_col]
        if s.dtype == bool:
            continue
        try:
            _ = s.map(bool)  # validation only
        except Exception as e:  # pragma: no cover
            raise ValueError(f"Gate column {gate_col!r} must be boolean/castable-to-bool.") from e

    # --- target: numeric when present, nonnegative
    y = pd.to_numeric(df[panel.y_col], errors="coerce")
    y_series = pd.Series(y)  # Ensure it's a Series
    if (y_series.dropna() < 0).any():  # Ensure dropna and comparison are on Series
        raise ValueError(f"Target column {panel.y_col!r} contains negative values.")

    # --- day/interval mode checks
    if panel.time_mode == "day_interval":
        if panel.periods_per_day is None:
            raise ValueError("periods_per_day must be provided for time_mode='day_interval'.")

        idx = pd.to_numeric(df[panel.interval_index_col], errors="coerce")
        idx_series = pd.Series(idx)  # Ensure idx is a Series
        if idx_series.isna().any():  # Ensure isna is called on a Series
            raise ValueError(
                f"interval_index_col {panel.interval_index_col!r} must be integer-like."
            )

        if (
            (idx_series < 0) | (idx_series >= panel.periods_per_day)
        ).any():  # Handle comparison on Series
            raise ValueError(
                f"interval_index_col {panel.interval_index_col!r} must be in "
                f"[0, {panel.periods_per_day - 1}]."
            )

    # --- timestamp mode checks
    if panel.time_mode == "timestamp":
        ts = pd.to_datetime(df[panel.ts_col], errors="coerce")
        if ts.isna().any():  # Ensure isna is called on a Series
            raise ValueError(f"ts_col {panel.ts_col!r} must be datetime-like (parsable).")
