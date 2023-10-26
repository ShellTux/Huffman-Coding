#!/usr/bin/env python3

from numpy import ndarray
from numpy.typing import NDArray
import numpy as np
import pandas as pd

if __name__ != "__main__":
    exit(0)

def variableAlphabet(
        values: ndarray,
        varNames: list[str],
        *,
        label: str
        ) -> NDArray[np.uint16]:
    labelValues = values[:, varNames.index(label)]

    return np.unique(labelValues).astype(np.uint16)

data = pd.read_excel('./assets/CarDataset.xlsx')
varNames = data.columns.values.tolist()
values = data.values

for label in varNames:
    print(variableAlphabet(values, varNames, label = label))
