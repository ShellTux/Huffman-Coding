from enum import Enum
from matplotlib.figure import Figure
from numpy._typing import NDArray
import matplotlib.pyplot as plt


class Marker(Enum):
    """
    A class representing the various marker styles available for scatter plots.

    Attributes:
        POINT (str): A tiny point marker.
        PIXEL (str): A pixel marker.
        CIRCLE (str): A circle marker.
        TRIANGLE_DOWN (str): A triangle pointing downwards marker.
        TRIANGLE_UP (str): A triangle pointing upwards marker.
        TRIANGLE_LEFT (str): A triangle pointing left marker.
        TRIANGLE_RIGHT (str): A triangle pointing right marker.
        ARROW_DOWN (str): An arrow pointing downwards marker.
        ARROW_UP (str): An arrow pointing upwards marker.
        ARROW_LEFT (str): An arrow pointing left marker.
        ARROW_RIGHT (str): An arrow pointing right marker.
        SQUARE (str): A square marker.
        PENTAGON (str): A pentagon marker.
        STAR (str): A star marker.
        HEXAGON1 (str): A hexagon marker.
        HEXAGON2 (str): A hexagon with two vertical sides marker.
        PLUS (str): A plus sign marker.
        CROSS (str): A cross marker.
        DIAMOND (str): A diamond marker.
        THIN_DIAMOND (str): A thin diamond marker.
    """
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
    """
    A class representing the various colors available for plots.

    Attributes:
        BLUE (str): A blue color.
        GREEN (str): A green color.
        PURPLE (str): A purple color.
        RED (str): A red color.
        YELLOW (str): A yellow color.
    """
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
        ) -> None:
    """
    A function to draw a scatter plot.

    Args:
        xValues (ndarray): The x-coordinates of the data points.
        yValues (ndarray): The y-coordinates of the data points.
        figure (Figure): The matplotlib figure to plot the data on.
        title (str, optional): The title of the plot. Defaults to None.
        xLabel (str, optional): The label for the x-axis. Defaults to None.
        yLabel (str, optional): The label for the y-axis. Defaults to None.
        color (Color, optional): The color of the data points. Defaults to Color.PURPLE.
        marker (Marker, optional): The marker style of the data points. Defaults to Marker.CIRCLE.
        grid (bool, optional): Whether to draw a grid on the plot. Defaults to True.
        subplot (int, optional): The subplot to plot the data on. Defaults to 111.

    Returns:
        None
    """
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
        ) -> None:
    """
    A function to draw a histogram.

    Args:
        xValues (ndarray): The x-values of the data points.
        yValues (ndarray): The y-values of the data points.
        title (str, optional): The title of the plot. Defaults to 'Histogram'.
        xLabel (str, optional): The label for the x-axis. Defaults to None.
        yLabel (str, optional): The label for the y-axis. Defaults to None.
        color (Color, optional): The color of the bars. Defaults to Color.RED.
        grid (bool, optional): Whether to draw a grid on the plot. Defaults to True.
        figure (Figure): The matplotlib figure to plot the data on.
        subplot (int, optional): The subplot to plot the data on. Defaults to 111.

    Returns:
        None
    """
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
