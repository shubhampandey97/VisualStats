from core.registry import VisualizationRegistry
from visualizations.histogram import render_histogram
from visualizations.boxplot import render_boxplot
from visualizations.kde import render_kde




def register_visualizations(registry: VisualizationRegistry) -> None:
    registry.register("Histogram", render_histogram)
    registry.register("Box Plot", render_boxplot)
    registry.register("KDE Density", render_kde)
