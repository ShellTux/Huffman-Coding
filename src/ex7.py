#!/usr/bin/env python3

from data import DATA
import numpy as np

if __name__ == "__main__":
    variables = DATA.getVariables()
    maxVariableLength = max(map(len, variables))
    for variable in variables:
        values = DATA.getValues(variable = variable)
        bps = DATA.bitsPerSymbol(variable = variable)
        print(f'{variable:<{maxVariableLength}} = {bps:.2f} bits/symbol')

    print()

    # All values
    valuesBPS = DATA.bitsPerSymbol()
    print(f'bps(values) = {valuesBPS:.2f} bits/symbol')
