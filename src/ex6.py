#!/usr/bin/env python3

from data import DATA

def main():
    variableBinSizePairs = (
            ('Weight', 40),
            ('Displacement', 5),
            ('Horsepower', 5),
            )
    for _, (variable, binSize) in enumerate(variableBinSizePairs):
        binnedData = DATA.binning(variable = variable, binSize = binSize)
        print(f'{variable}:', binnedData, sep = '\n', end = '\n' * 2)
