#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from data import variableValues, values, varNames

if __name__ != "__main__":
    exit(0)

print(varNames)
print(values)
MPGValues = variableValues(values,varNames,'MPG')
plt.figure('ex2')
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
for index, variable in enumerate(varNames[:-1]):
    varValues = variableValues(values,varNames,variable)
    plt.subplot(int(f'32{index+1}'))
    plt.xlabel(variable)
    plt.ylabel('MPG')
    plt.scatter(varValues, MPGValues, color = 'purple')
    plt.title(f'MPG vs. {variable}')
plt.show()
