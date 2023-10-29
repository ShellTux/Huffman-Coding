#!/usr/bin/env python3

from data import DATA

if __name__ == "__main__":
    for variable in DATA.getVariables():
        values = DATA.getValues(variable = variable)
        _, alphabetCount = DATA.getAlphabet(variable = variable, returnCount = True)

        print(f'{variable}:', alphabetCount, sep = '\n', end = '\n' * 2)
