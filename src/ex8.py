#!/usr/bin/env python3

from data import DATA


if __name__ == "__main__":
    for variable in DATA.getVariables():
        avgBits = DATA.averageBitsPerSymbol(variable = variable)
        lengthVariance = DATA.lengthVariance(variable = variable)

        print(
                variable,
                f'{f"Average bits per symbol:":<{24}} {avgBits:.3f}',
                f'{f"Variance of lengths:":<{24}} {lengthVariance:.3f}',
                sep = '\n',
                end = '\n' * 2
                )
