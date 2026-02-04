from core.registry import VisualizationRegistry
from visualizations import register_visualizations


def test_histogram_is_registered():
    registry = VisualizationRegistry()
    register_visualizations(registry)

    available = registry.list_available()
    assert "Histogram" in available
