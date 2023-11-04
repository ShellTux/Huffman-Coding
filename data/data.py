from numpy._typing import NDArray, DTypeLike
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
    getVariables
    getValues
    getAlphabet
    getProbabilities
    getJointProbability
    bitsPerSymbol
    averageBitsPerSymbol
    lengthVariance
    binning
    mostRepresentativeSymbol
    pearsonCoeficient
    mutualInformation
    """

    def __init__(self, excelFilepath: str, dataType: DTypeLike) -> None:
        """
        Constructs all the necessary attributes for the Data object.

        Parameters
        ----------
            excelFilepath : str
                File path of the excel file containing the data

            dataType: DTypeLike
                Data type of elements of excel matrix
        """

        # Read the excel file and store the values
        data = pd.read_excel(excelFilepath)
        self.__VARIABLES: list[str] = data.columns.values.tolist()
        self.__VALUES: NDArray = data.values.copy().astype(dataType)

        # Create mapping between variables and their values
        self.__mapVariableValues: Dict[str, NDArray[np.uint16]] = dict()
        for index, variable in enumerate(self.__VARIABLES):
            values = self.__VALUES[:, index].copy().astype(dataType)
            self.__mapVariableValues[variable] = values

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
        Returns the matrix of values present in the excel sheet,
        or if a variable is specified, returns its values.

        Parameters
        ----------
        variable : str, optional
            The variable whose values are required. If not specified, all values
            present in the excel sheet are returned. (default None)

        Raises
        ------
        KeyError
            If the specified variable is not present in the excel sheet

        Returns
        -------
        numpy.ndarray
            Matrix of values present in the excel sheet, or if a variable is
            specified, its values
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
        Returns the unique values present in the excel sheet as an array or, if
        a variable is specified, its unique values along with their counts as a
        tuple.

        Parameters
        ----------
        variable : str, optional
            The variable whose unique values are required. If not specified, all
            unique values present in the excel sheet are returned.
            (default None)
        returnCount : bool, optional
            Whether to return the counts of the unique values along with the
            array of unique values. (default False)

        Returns
        -------
        numpy.ndarray | tuple[numpy.ndarray, numpy.ndarray]
            An array of unique values present in the excel sheet or, if a
            variable is specified, its unique values along with their counts as
            a tuple
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

    def getProbabilities(
            self,
            *,
            variable: str | None = None,
            ) -> NDArray[np.floating]:
        """
        Returns the probability of each value present in the excel sheet,
        or if a variable is specified, returns its probability distribution

        Parameters
        ----------
        variable : str, optional
            The variable whose values are to be used
            for calculating the probability distribution.
            If not specified, all values present in the excel sheet are used.
            (default None)

        Returns
        -------
        numpy.ndarray
            An array of the probabilities of each value in the excel sheet,
            or if a variable is specified, its probability distribution
        """
        values = self.getValues(variable = variable)

        if values.ndim > 1:
            values = values.flatten()

        probabilities = np.bincount(values) / values.size

        return probabilities

    def getJointProbability(
            self,
            *,
            variable1: str,
            variable2: str,
            ) -> NDArray[np.floating]:
        """
        Returns the joint probability distribution of variable1 and variable2 as
        a numpy array

        Parameters
        ----------
        variable1 : str
            The first variable
        variable2 : str
            The second variable

        Returns
        -------
        numpy.ndarray
            The joint probability distribution of variable1 and variable2 as a
            numpy array
        """

        probabilities1 = self.getProbabilities(variable = variable1)
        probabilities2 = self.getProbabilities(variable = variable2)

        # NOTE: Assuming independence
        return probabilities1 * probabilities2

    def bitsPerSymbol(self, *, variable: str | None = None) -> np.floating:
        """
        Returns the number of bits per symbol required to represent the values
        present in the excel sheet or, if a variable is specified, its values.

        Parameters
        ----------
        variable : str, optional
            The variable whose values are to be used for calculating the number
            of bits per symbol. If not specified, all values present in the
            excel sheet are used. (default None)

        Returns
        -------
        float
            The number of bits per symbol required to represent the values
            present in the excel sheet or, if a variable is specified, its
            values.
        """

        probabilities = self.getProbabilities(variable = variable)
        probabilities = probabilities[probabilities > 0]

        # NOTE: Entropy H = -sum(p * log2(p))
        return -np.sum(probabilities * np.log2(probabilities))

    def averageBitsPerSymbol(
            self,
            *,
            variable: str | None = None
            ) -> np.floating:
        """
        Returns the average number of bits per symbol required to encode the
        values in the excel sheet using Huffman encoding, or if a variable is
        specified, its values

        Parameters
        ----------
        variable : str, optional
            The variable whose values are to be used for calculating the number
            of bits per symbol. If not specified, all values present in the
            excel sheet are used. (default None)

        Returns
        -------
        numpy.floating
            The average number of bits per symbol required to encode the values
            in the excel sheet using Huffman encoding, or if a variable is
            specified, its values

        """
        S = self.getValues(variable = variable)

        if S.ndim > 1:
            S = S.flatten()

        codec = huffc.HuffmanCodec.from_data(S)
        _, lengths = codec.get_code_len()

        probabilities = self.getProbabilities(variable = variable)
        probabilities = probabilities[probabilities > 0]

        return np.average(lengths, weights = probabilities)

    # TODO: Remove duplicated code between lengthVariance and averageBitsPerSymbol
    def lengthVariance(self, *, variable: str | None = None) -> np.floating:
        """
        Returns the variance of the lengths of the Huffman codes required to
        encode the values in the excel sheet, or if a variable is specified, its
        values

        Parameters
        ----------
        variable : str, optional (default None)
            The variable whose values are to be used for calculating the
            variance of the lengths of the Huffman codes. If not specified, all
            values present in the excel sheet are used.

        Returns
        -------
        np.floating
            The variance of the lengths of the Huffman codes required to encode
            the values in the excel sheet, or if a variable is specified, its
            values
        """
        S = self.getValues(variable = variable)

        if S.ndim > 1:
            S = S.flatten()

        codec = huffc.HuffmanCodec.from_data(S)
        _, lengths = codec.get_code_len()

        return np.var(lengths)


    def binning(self, *, binSize: int, variable: str | None = None) -> NDArray:
        """
        Returns the values in the excel sheet, or if a variable is specified,
        its values, divided into bins of size binSize The value in each bin is
        replaced by its most representative symbol

        Parameters
        ----------
        binSize : int
            The size of each bin
        variable : str, optional
            The variable whose values are to be binned. If not specified, all
            values in the excel sheet are binned. (default None)

        Returns
        -------
        numpy.ndarray
            The values in the excel sheet, or if a variable is specified, its
            values, divided into bins of size binSize, with each value in a bin
            replaced by its most representative symbol
        """
        values = self.getValues(variable = variable)
        alphabet, _ = self.getAlphabet(variable = variable, returnCount=True)

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
        """
        Returns the most representative symbol in the excel sheet, or if a
        variable is specified, its values

        Parameters
        ----------
        variable : str, optional (default None)
            The variable whose most representative symbol is to be returned. If
            not specified, the most representative symbol of all values in the
            excel sheet is returned.

        Returns
        -------
        int or float
            The most representative symbol in the excel sheet, or if a variable
            is specified, its values
        """
        values = self.getValues(variable = variable)

        return mostRepresentativeSymbol(values = values)

    def pearsonCoeficient(
            self,
            *,
            variableX: str,
            variableY: str,
            ) -> float | None:
        """
        Returns the Pearson correlation coefficient between
        variableX and variableY in the excel sheet

        Parameters
        ----------
        variableX : str
            The first variable
        variableY : str
            The second variable

        Returns
        -------
        float or None
            The Pearson correlation coefficient between
            variableX and variableY in the excel sheet,
            or None if either of the variables is not present
            in the excel sheet
        """
        if variableX is None or variableY is None:
            return

        valuesX = self.getValues(variable = variableX)
        valuesY = self.getValues(variable = variableY)

        return np.corrcoef(valuesX, valuesY)[0,1]

    def mutualInformation(
            self,
            *,
            variableX: str,
            variableY: str,
            ) -> float:
        """
        Returns the mutual information between variableX and variableY in the
        excel sheet

        Parameters
        ----------
        variableX : str
            The first variable
        variableY : str
            The second variable

        Returns
        -------
        float
            The mutual information between variableX and variableY in the excel
            sheet
        """
        X = self.getValues(variable = variableX)
        Y = self.getValues(variable = variableY)

        # compute the unique values of X and Y and their counts
        alphabetX, countX = self.getAlphabet(variable = variableX, returnCount = True)
        alphabetY, countY = self.getAlphabet(variable = variableY, returnCount = True)

        # compute the counts for each (X,Y) pair based on their unique indices
        indexX = np.searchsorted(alphabetX, X)
        indexY = np.searchsorted(alphabetY, Y)
        jointCounts = np.zeros((alphabetX.size, alphabetY.size))
        for xIndex, yIndex in zip(indexX, indexY):
            jointCounts[xIndex, yIndex] += 1

        # compute the probabilities of X, Y and their joint probability
        probabilitiesX = countX / X.size
        probabilitiesY = countY / Y.size
        jointProbabilityXY = jointCounts / X.size

        # compute the mutual information
        # TODO: Use single for loop
        mutualInformation = 0
        for i in range(alphabetX.size):
            for j in range(alphabetY.size):
                px = probabilitiesX[i]
                py = probabilitiesY[j]
                pxy = jointProbabilityXY[i, j]
                if pxy > 0:
                    mutualInformation += pxy * np.log2(pxy / (px * py))

        return mutualInformation
