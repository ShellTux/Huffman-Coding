#!/usr/bin/env python3

from data import DATA


if __name__ == "__main__":
    MI = DATA.mutualInformation(
            variableX = 'MPG',
            variableY = 'Weight',
            )
    print(MI)
