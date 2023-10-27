from numpy import ndarray
from numpy._typing import NDArray
from typing import Dict
import numpy as np
import pandas as pd

class Data:
    def __init__(self, excelFilepath: str) -> None:
        data = pd.read_excel(excelFilepath)
        self.__VARIABLES: list[str] = data.columns.values.tolist()
        self.__VALUES: NDArray = data.values.copy()

        # Create mapping between variable and their values
        self.__mapVariableValues: Dict[str, NDArray] = dict()
        for index, variable in enumerate(self.__VARIABLES):
            self.__mapVariableValues[variable] = self.__VALUES[:, index].copy()

    def getVariables(self) -> list[str]:
        return self.__VARIABLES[:]

    def getValues(self, *, variable: str | None = None) -> NDArray:
        if variable is None:
            return self.__VALUES.copy()

        values = self.__mapVariableValues.get(variable)

        if values is None:
            raise KeyError(f'There is no \'{variable}\' in {self.__VARIABLES}')

        return values.copy()

    def getAlphabet(
            self, *,
            variable: str | None = None,
            returnCount: bool = False
            ) -> NDArray | tuple[NDArray, NDArray[np.intp]]:
        if variable is None:
            if returnCount:
                return np.unique(self.__VALUES, return_counts = True)
            else:
                return np.unique(self.__VALUES)

        values = self.getValues(variable = variable)

        if returnCount:
            return np.unique(values, return_counts = True)
        else:
            return np.unique(values)

    def bitsPerSymbol(self, *, variable: str | None = None):
        values = self.getValues(variable = variable).flatten()
        probabilities = np.bincount(values) / values.size
        probabilities = probabilities[probabilities > 0]

        # NOTE: Entropy H = -sum(p * log2(p))
        return -np.sum(probabilities * np.log2(probabilities))



DATA = Data('./assets/CarDataset.xlsx')
