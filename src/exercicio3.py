#!/usr/bin/env python3

from data import variableAlphabet, values, varNames

for variable in varNames:
    print(variable)
    print(variableAlphabet(values, varNames,variable))
    print()