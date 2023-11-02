from numpy._typing import NDArray
from typing import Dict
import huffmancodec.huffmancodec as huffc
import numpy as np
import pandas as pd

def mostRepresentativeSymbol(*, values: NDArray):
    alphabet, alphabetCount = np.unique(values.flatten(), return_counts = True)

    maxIndex = np.argmax(alphabetCount)
    return alphabet[maxIndex]

class Data:
    """
    This class is used to read an excel file and store data and provide access to it.

    ...

    Attributes
    ----------
    __VARIABLES : list[str]
        List of column names present in the excel sheet
    __VALUES : numpy.ndarray
        Matrix of values present in the excel sheet
    __mapVariableValues : Dict[str, numpy.ndarray]
        Dictionary of variables with their respective values

    Methods
    -------
    getVariables() -> list[str]:
        Returns the list of column names present in the excel sheet
    getValues(variable: str | None = None) -> numpy.ndarray:
        Returns the matrix of values present in the excel sheet, or if a variable is specified, returns its values
    getAlphabet(variable: str | None = None, returnCount: bool = False) -> numpy.ndarray | tuple[numpy.ndarray, numpy.ndarray]:
        Returns the unique values present in the excel sheet as an array or, if a variable is specified, its unique values
        along with their counts as a tuple
    bitsPerSymbol(variable: str | None = None)
        Returns the number of bits per symbol required to represent the values present in the excel sheet or, if a variable
        is specified, its values
    """

    def __init__(self, excelFilepath: str) -> None:
        """
        Constructs all the necessary attributes for the Data object.

        Parameters
        ----------
            excelFilepath : str
                File path of the excel file containing the data
        """

        # Read the excel file and store the values
        data = pd.read_excel(excelFilepath)
        self.__VARIABLES: list[str] = data.columns.values.tolist()
        self.__VALUES: NDArray = data.values.copy()

        # Create mapping between variables and their values
        self.__mapVariableValues: Dict[str, NDArray] = dict()
        for index, variable in enumerate(self.__VARIABLES):
            self.__mapVariableValues[variable] = self.__VALUES[:, index].copy()

    def getVariables(self) -> list[str]:
        """
        Returns the list of column names present in the excel sheet.

        Returns
        -------
        list[str]
            List of column names present in the excel sheet
        """

        return self.__VARIABLES[:]

    def getValues(self, *, variable: str | None = None) -> NDArray:
        """
        Returns the matrix of values present in the excel sheet, or if a variable is specified, returns its values.

        Parameters
        ----------
        variable : str, optional
            The variable whose values are required. If not specified, all values present in the excel sheet are returned. (default None)

        Raises
        ------
        KeyError
            If the specified variable is not present in the excel sheet

        Returns
        -------
        numpy.ndarray
            Matrix of values present in the excel sheet, or if a variable is specified, its values
        """

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
        """
        Returns the unique values present in the excel sheet as an array or, if a variable is specified, its unique values
        along with their counts as a tuple.

        Parameters
        ----------
        variable : str, optional
            The variable whose unique values are required. If not specified, all unique values present in the excel sheet are returned. (default None)
        returnCount : bool, optional
            Whether to return the counts of the unique values along with the array of unique values. (default False)

        Returns
        -------
        numpy.ndarray | tuple[numpy.ndarray, numpy.ndarray]
            An array of unique values present in the excel sheet or, if a variable is specified, its unique values
            along with their counts as a tuple
        """

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
        """
        Returns the number of bits per symbol required to represent the values present in the excel sheet or, if a variable
        is specified, its values.

        Parameters
        ----------
        variable : str, optional
            The variable whose values are to be used for calculating the number of bits per symbol. If not specified,
            all values present in the excel sheet are used. (default None)

        Returns
        -------
        float
            The number of bits per symbol required to represent the values present in the excel sheet or, if a variable
            is specified, its values.
        """

        values = self.getValues(variable = variable).flatten()
        probabilities = np.bincount(values) / values.size
        probabilities = probabilities[probabilities > 0]

        # NOTE: Entropy H = -sum(p * log2(p))
        return -np.sum(probabilities * np.log2(probabilities))

    def averageBitsPerSymbol(self, *,
            variable: str | None = None
            ) -> np.floating:
        S = self.getValues(variable = variable)
        codec = huffc.HuffmanCodec.from_data(S)
        _, lengths = codec.get_code_len()

        probabilities = np.bincount(S) / S.size
        probabilities = probabilities[probabilities > 0]

        return np.average(lengths, weights = probabilities)

    # TODO: Remove duplicated code between lengthVariance and averageBitsPerSymbol
    def lengthVariance(self, *, variable: str | None = None) -> np.floating:
        S = self.getValues(variable = variable)
        codec = huffc.HuffmanCodec.from_data(S)
        _, lengths = codec.get_code_len()

        return np.var(lengths)


    def binning(self, *,
                binSize: int,
                variable: str | None = None,
                ) -> NDArray:
        values = self.getValues(variable = variable)
        alphabet, _ = self.getAlphabet(
                variable = variable,
                returnCount=True
                )

        # Binning Algorithm
        min, max = alphabet[0], alphabet[0] + binSize - 1
        maxAlphabet = alphabet[-1]
        while min < maxAlphabet:
            valuesFilter: NDArray[np.bool_] = (min <= values) & (values <= max)

            alphabetFilter: NDArray[np.bool_] = (min <= alphabet) & (alphabet <= max)
            alphabetSection = alphabet[alphabetFilter]

            if alphabetSection.size <= 0:
                min += binSize
                max += binSize
                continue

            symbol = mostRepresentativeSymbol(values = alphabetSection)

            values = np.where(valuesFilter, symbol, values)

            min += binSize
            max += binSize

        return values

    def mostRepresentativeSymbol(
            self, *,
            variable: str | None = None
            ) -> int | float:
        values = self.getValues(variable = variable)

        return mostRepresentativeSymbol(values = values)
