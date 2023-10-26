from data import variableValues
from matplotlib.figure import Figure
from numpy import ndarray
import matplotlib.pyplot as plt

def scatter(
        values: ndarray, varNames: list[str],
        *,
        title: str | None = None,
        xLabel: str,
        yLabel: str,
        color: str = 'purple',
        marker: str = 'o',
        grid: bool = True,
        figure: Figure,
        subplot: int = 111,
        ):
    if title is None:
        title = f'{yLabel} vs {xLabel}'

    plt.figure(figure)
    plt.subplot(subplot)
    xValues = variableValues(values, varNames, label = xLabel)
    yValues = variableValues(values, varNames, label = yLabel)
    plt.scatter(xValues, yValues, color = color, marker = marker)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(grid)

def histogram(
        alphabet: ndarray,
        values: ndarray,
        *,
        title: str = 'Histogram',
        xLabel: str,
        yLabel: str,
        color: str = 'red',
        grid: bool = True,
        figure: Figure,
        subplot: int = 111,
        ):
    plt.figure(figure)
    plt.subplot(subplot)
    # TODO: x values are float
    print(alphabet.dtype)
    plt.bar(alphabet, values, color = color)
    # TODO: add occurrences for intermidiate values (plt.xticks)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(grid)
