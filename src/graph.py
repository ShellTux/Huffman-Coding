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
        subplot: int,
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
