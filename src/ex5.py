#!/usr/bin/env python3

from data import DATA
from graph import histogram
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    figure = plt.figure('Histogram')
    variable = 'Acceleration'
    values = DATA.getValues(variable = variable).astype(np.uint16)
    alphabet, alphabetCount = DATA.getAlphabet(
            variable    = variable,
            returnCount = True
            )
    print(alphabet, alphabetCount, sep = '\n')
    histogram(
            xValues = alphabet,
            yValues = alphabetCount,
            xLabel  = variable,
            yLabel  = 'Count',
            figure  = figure,
            )

    plt.show()

    figure.subplots_adjust(wspace = .5, hspace = .5)
    figure.savefig('Ex5.png')
