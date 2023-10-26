#!/usr/bin/env python3

from numpy import ndarray
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from data import varNames, values

if __name__ != "__main__":
    exit(0)

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
    xValues = values[:, varNames.index(xLabel)]
    yValues = values[:, varNames.index(yLabel)]
    plt.scatter(xValues, yValues, color = color, marker = marker)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(grid)

figure, _ = plt.subplots(nrows = 3, ncols = 2)
figure.suptitle('Ex2')
figure.subplots_adjust(wspace=0.5, hspace=0.5)
variablePairs = (
        ('Acceleration', 'MPG'),
        ('Cylinders', 'MPG'),
        ('Displacement', 'MPG'),
        ('Horsepower', 'MPG'),
        ('ModelYear', 'MPG'),
        ('Weight', 'MPG'),
        )
for index, (xLabel, yLabel) in enumerate(variablePairs):
    # TODO: adjust subplot size according to variablePairs size
    scatter(values, varNames, xLabel = xLabel, yLabel = yLabel,
            figure = figure,
            subplot = int(f'32{index+1}'))

plt.show()
