#!/usr/bin/env python3

from src.ex10 import main as ex10
from src.ex11 import main as ex11
from src.ex2 import main as ex2
from src.ex3 import main as ex3
from src.ex4 import main as ex4
from src.ex5 import main as ex5
from src.ex6 import main as ex6
from src.ex7 import main as ex7
from src.ex8 import main as ex8
from src.ex9 import main as ex9
from colors import GREEN, RESET
import sys

if __name__ == "__main__":
    exercices = (
        (2, ex2),
        (3, ex3),
        (4, ex4),
        (5, ex5),
        (6, ex6),
        (7, ex7),
        (8, ex8),
        (9, ex9),
        (10, ex10),
        (11, ex11),
    )

    arguments = sys.argv[1:]
    exercises = []
    for index, argument in enumerate(arguments):
        try:
            exercises.append(int(argument))
        except ValueError:
            print(f"Error: '{argument}' is not a valid number.")

    for number, main in exercices:
        if len(exercises) != 0 and number not in exercises:
            continue

        print()
        print(GREEN + f"-------Ex{number}-------" + RESET)
        main()
        print()
