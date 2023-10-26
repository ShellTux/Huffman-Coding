#!/usr/bin/env python3

from data import values, variableAlphabet, variableValues, varNames
from ex4 import alphabetOccurrenceCount
from graph import histogram
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    figure = plt.figure('Histogram')
    label = 'Acceleration'
    accelerationValues = variableValues(values, varNames, label =
                                        label).astype(np.uint16)
    accelerationAlphabet = variableAlphabet(values, varNames, label = label)
    accelerationAlphabetOccurrence = alphabetOccurrenceCount(accelerationValues)
    histogram(
            accelerationAlphabet,
            accelerationAlphabetOccurrence,
            xLabel = 'Acceleration',
            yLabel = 'Count',
            figure = figure
            )
    plt.show()
