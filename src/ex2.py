#!/usr/bin/env python3

from data import varNames, values
from graph import scatter
import matplotlib.pyplot as plt

if __name__ != "__main__":
    exit(0)

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

plt.savefig('Ex2.png')
plt.show()
