#!/usr/bin/env python3

from data import variableAlphabetCount, values, varNames


for variable in varNames:
    print(variable)
    print(variableAlphabetCount(values, varNames, variable))
    print()