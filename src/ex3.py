#!/usr/bin/env python3

from data import values, varNames, variableAlphabet

if __name__ == "__main__":
    for label in varNames:
        print(f'{label}:', variableAlphabet(values, varNames, label = label),
              sep = '\n',
              end = '\n\n',
              )
