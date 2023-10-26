#!/usr/bin/env python3

import data
from data import variableValues

if __name__ == "__main__":
    for variable in data.varNames:
        values = variableValues(data.values, data.varNames, label = variable)
        bitsMean = data.bits_per_symbol(values)
        print(f'{variable} = {bitsMean:.2f} bits/symbol')

    print()

    # All values
    valuesFlatten = data.values.flatten()
    valuesBPS = data.bits_per_symbol(valuesFlatten)
    print(f'bps(values) = {valuesBPS:.2f} bits/symbol')
