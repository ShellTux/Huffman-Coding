#!/usr/bin/env python3

from data import DATA

if __name__ == "__main__":
    variableBinSizePairs = (
            ('Weight', 40),
            ('Displacement', 5),
            ('Horsepower', 5),
            )
    for index, (variable, binSize) in enumerate(variableBinSizePairs):
        alphabet = DATA.getAlphabet(variable = variable)
        binnedData = DATA.binning(variable = variable, binSize = binSize)
        print(f'{variable}:', binnedData, sep = '\n', end = '\n' * 2)
