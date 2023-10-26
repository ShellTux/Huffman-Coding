from numpy import ndarray
from numpy._typing import NDArray
import numpy as np
import pandas as pd

data = pd.read_excel('./assets/CarDataset.xlsx')
varNames: list[str] = data.columns.values.tolist()
values = data.values

def variableValues(
        values: ndarray,
        varNames: list[str],
        *,
        label: str,
        ) -> ndarray:
    return values[:, varNames.index(label)]


def variableAlphabet(
        values: ndarray,
        varNames: list[str],
        *,
        label: str
        ) -> NDArray[np.uint16]:
    labelValues = variableValues(values, varNames, label = label)

    return np.unique(labelValues).astype(np.uint16)

def bits_per_symbol(values: NDArray):
    probabilities = np.bincount(values) / values.size
    probabilities = probabilities[probabilities > 0]

    # Compute the entropy using the formula H = -sum(p * log2(p))
    return -np.sum(probabilities * np.log2(probabilities))
