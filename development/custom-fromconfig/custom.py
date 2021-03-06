"""Custom FromConfig implementation."""

import fromconfig


class MyClass(fromconfig.FromConfig):
    """Custom FromConfig implementation."""

    def __init__(self, x):
        self.x = x

    @classmethod
    def fromconfig(cls, config):
        # NOTE: config is not recursively instantiated yet
        config = {key: fromconfig.fromconfig(value) for key, value in config.items()}
        if "x" not in config:
            return cls(0)
        else:
            return cls(**config)


if __name__ == "__main__":
    cfg = {}
    got = MyClass.fromconfig(cfg)
    assert isinstance(got, MyClass)
    assert got.x == 0
