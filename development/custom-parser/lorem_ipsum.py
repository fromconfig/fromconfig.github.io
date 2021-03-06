"""Custom Parser that replaces empty string by a default string."""

from typing import Any

import fromconfig


class LoremIpsumParser(fromconfig.parser.Parser):
    """Custom Parser that replaces empty string by a default string."""

    def __init__(self, default: str = "lorem ipsum"):
        self.default = default

    def __call__(self, config: Any):
        def _map_fn(value):
            if isinstance(value, str) and not value:
                return self.default
            return value

        # Utility to apply a function to all nodes of a nested dict
        # in a depth-first search
        return fromconfig.utils.depth_map(_map_fn, config)


if __name__ == "__main__":
    cfg = {"x": "Hello World", "y": ""}
    parser = LoremIpsumParser()
    parsed = parser(cfg)
    assert parsed["y"] == parser.default
