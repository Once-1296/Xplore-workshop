"""Matplotlib plotting exercises (advanced).

Create a few helper functions that generate common plots:
- bar_chart(labels, values)
- scatter_plot(x, y)
- histogram(values, bins=10)

Each function should optionally accept a `show` argument (default False)
so unit tests can inspect the created Figure object.
"""


def bar_chart(labels, values, show: bool = False):
    """Create and return a bar chart for given labels and values.

    If matplotlib is available, return the Figure; otherwise raise ImportError.
    """
    raise NotImplementedError()


def scatter_plot(x, y, show: bool = False):
    """Create and return a scatter plot Figure for x vs y.
    """
    raise NotImplementedError()


def histogram(values, bins: int = 10, show: bool = False):
    """Create and return a histogram Figure for values.
    """
    raise NotImplementedError()


if __name__ == "__main__":
    print("This module contains matplotlib exercises. Implement the plotting helpers.")

