#!/usr/bin/env python3

from data import DATA

if __name__ == "__main__":
    for variable in DATA.getVariables():
        values = DATA.getValues(variable = variable)
        bps = DATA.bitsPerSymbol(variable = variable)
        print(f'{variable} = {bps:.2f} bits/symbol')

    print()

    # All values
    valuesFlatten = DATA.getValues().flatten()
    valuesBPS = DATA.bitsPerSymbol()
    print(f'bps(values) = {valuesBPS:.2f} bits/symbol')
