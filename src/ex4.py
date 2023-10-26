#!/usr/bin/env python3

from data import variableValues
from numpy.typing import NDArray
import data
import numpy as np

def alphabetOccurrenceCount(variableValues: NDArray) -> NDArray:
    max: int = variableValues.max()

    # NOTE: count is positive so an arbitrary unsigned type is valid
    # NOTE: count is a nparray counting every symbol occurrence
    # every index is mapped to a symbol.
    # Example: the number of occurrences of symbol 17 is given by count[17]
    # WARNING: count assumes the alphabet contains only non-negative numbers
    count: NDArray = np.zeros(max + 1, dtype = np.uint32)

    for symbol in variableValues:
        count[symbol] += 1

    count = count[count != 0]

    return count

if __name__ == "__main__":
    for variable in data.varNames:
        values = variableValues(data.values, data.varNames, label = variable)
        alphabetCount = alphabetOccurrenceCount(values)

        print(f'{variable}:', alphabetCount, sep = '\n', end = '\n' * 2)
