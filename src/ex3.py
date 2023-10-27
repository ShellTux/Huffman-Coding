#!/usr/bin/env python3

from data import DATA

if __name__ == "__main__":
    for variable in DATA.getVariables():
        print(f'{variable}:', DATA.getAlphabet(variable = variable),
              sep = '\n',
              end = '\n\n',
              )
