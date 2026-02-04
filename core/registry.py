from typing import Callable, Dict


class VisualizationRegistry:
    """
    Central registry for all visualizations.
    Each visualization registers itself with a name and a render function.
    """

    def __init__(self) -> None:
        self._visualizations: Dict[str, Callable] = {}

    def register(self, name: str, render_fn: Callable) -> None:
        if name in self._visualizations:
            raise ValueError(f"Visualization '{name}' is already registered.")
        self._visualizations[name] = render_fn

    def get(self, name: str) -> Callable:
        if name not in self._visualizations:
            raise KeyError(f"Visualization '{name}' not found.")
        return self._visualizations[name]

    def list_available(self) -> list[str]:
        return sorted(self._visualizations.keys())
