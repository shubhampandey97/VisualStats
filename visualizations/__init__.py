from core.registry import VisualizationRegistry
from visualizations.histogram import render_histogram


def register_visualizations(registry: VisualizationRegistry) -> None:
    registry.register("Histogram", render_histogram)
