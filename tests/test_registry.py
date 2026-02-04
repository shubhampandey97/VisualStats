import pytest
from core.registry import VisualizationRegistry


def dummy_render(data, config):
    pass


def test_register_and_get_visualization():
    registry = VisualizationRegistry()
    registry.register("histogram", dummy_render)

    render_fn = registry.get("histogram")
    assert render_fn is dummy_render


def test_register_duplicate_visualization_raises_error():
    registry = VisualizationRegistry()
    registry.register("histogram", dummy_render)

    with pytest.raises(ValueError):
        registry.register("histogram", dummy_render)


def test_get_unknown_visualization_raises_error():
    registry = VisualizationRegistry()

    with pytest.raises(KeyError):
        registry.get("unknown")


def test_list_available_visualizations():
    registry = VisualizationRegistry()
    registry.register("histogram", dummy_render)
    registry.register("boxplot", dummy_render)

    available = registry.list_available()
    assert available == ["boxplot", "histogram"]
