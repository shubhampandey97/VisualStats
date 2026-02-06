"""
Central configuration for Statistics Explorer.
Acts as single source of truth for runtime behavior.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    # ---- Data ----
    default_sample_size: int = 10_000
    random_seed: int = 42

    # ---- Skewness ----
    skew_threshold: float = 0.5

    # ---- Visualization ----
    default_bins: int = 15
    min_bins: int = 5
    max_bins: int = 50

    # ---- Logging ----
    log_level: str = "INFO"
    log_file: str = "app.log"


CONFIG = AppConfig()
