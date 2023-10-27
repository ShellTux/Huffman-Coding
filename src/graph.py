from enum import Enum
from matplotlib.figure import Figure
from numpy import ndarray
from numpy._typing import NDArray
import matplotlib.pyplot as plt


class Marker(Enum):
    POINT = '.'
    PIXEL = ','
    CIRCLE = 'o'
    TRIANGLE_DOWN = 'v'
    TRIANGLE_UP = '^'
    TRIANGLE_LEFT = '<'
    TRIANGLE_RIGHT = '>'
    ARROW_DOWN = '1'
    ARROW_UP = '2'
    ARROW_LEFT = '3'
    ARROW_RIGHT = '4'
    SQUARE = 's'
    PENTAGON = 'p'
    STAR = '*'
    HEXAGON1 = 'h'
    HEXAGON2 = 'H'
    PLUS = '+'
    CROSS = 'x'
    DIAMOND = 'D'
    THIN_DIAMOND = 'd'

class Color(Enum):
    BLUE = 'blue'
    GREEN = 'green'
    PURPLE = 'purple'
    RED = 'red'
    YELLOW = 'yellow'


def scatter(
        *,
        xValues: NDArray, yValues: NDArray,
        figure: Figure,
        title: str | None = None,
        xLabel: str | None = None,
        yLabel: str | None = None,
        color: Color = Color.PURPLE,
        marker: Marker = Marker.CIRCLE,
        grid: bool = True,
        subplot: int = 111,
        ):
    if title is None:
        if xLabel is not None and yLabel is not None:
            title = f'{yLabel} vs {xLabel}'

    plt.figure(figure)

    plt.subplot(subplot)
    plt.scatter(xValues, yValues, color = color.value, marker = marker.value)

    if title is not None:
        plt.title(title)

    if xLabel is not None:
        plt.xlabel(xLabel)

    if yLabel is not None:
        plt.ylabel(yLabel)

    plt.grid(grid)

def histogram(
        *,
        xValues: NDArray,
        yValues: NDArray,
        title: str = 'Histogram',
        xLabel: str | None = None,
        yLabel: str | None = None,
        color: Color = Color.RED,
        grid: bool = True,
        figure: Figure,
        subplot: int = 111,
        ):
    plt.figure(figure)
    plt.subplot(subplot)

    # TODO: x values are float
    plt.bar(xValues, yValues, color = color.value)
    # TODO: add occurrences for intermidiate values (plt.xticks)

    plt.title(title)

    if xLabel is not None:
        plt.xlabel(xLabel)

    if yLabel is not None:
        plt.ylabel(yLabel)

    plt.grid(grid)
