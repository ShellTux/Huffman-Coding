#!/usr/bin/env python3

from data import values, varNames, variableValues
from numpy import ndarray
from numpy.typing import NDArray
import numpy as np

def variableAlphabet(
        values: ndarray,
        varNames: list[str],
        *,
        label: str
        ) -> NDArray[np.uint16]:
    labelValues = variableValues(values, varNames, label = label)

    return np.unique(labelValues).astype(np.uint16)

if __name__ == "__main__":
    for label in varNames:
        print(f'{label}:', variableAlphabet(values, varNames, label = label),
              sep = '\n',
              end = '\n\n',
              )
