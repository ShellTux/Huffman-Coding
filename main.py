#!/usr/bin/env python3

from src.ex2 import main as ex2
from src.ex3 import main as ex3
from src.ex4 import main as ex4
from src.ex5 import main as ex5
from src.ex6 import main as ex6
from src.ex7 import main as ex7
from src.ex8 import main as ex8

GREEN = '\033[32m'
RESET = '\033[0m'

if __name__ == "__main__":
    exercices = (
            ('Ex2', ex2),
            ('Ex3', ex3),
            ('Ex4', ex4),
            ('Ex5', ex5),
            ('Ex6', ex6),
            ('Ex7', ex7),
            ('Ex8', ex8),
            )

    for name, main in exercices:
        print()
        print(GREEN + f'-------{name}-------' + '\033[0m')
        main()
        print()
