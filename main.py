#!/usr/bin/env python3

from src.ex2 import main as ex2
from src.ex3 import main as ex3
from src.ex4 import main as ex4
from src.ex5 import main as ex5
from src.ex6 import main as ex6
from src.ex7 import main as ex7
from src.ex8 import main as ex8


if __name__ == "__main__":
    exercices = (
            ex2,
            ex3,
            ex4,
            ex5,
            ex6,
            ex7,
            ex8,
            )

    for main in exercices:
        main()
