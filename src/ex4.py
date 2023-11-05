from data import DATA


def main():
    for variable in DATA.getVariables():
        _, alphabetCount = DATA.getAlphabet(variable=variable, returnCount=True)

        print(f"{variable}:", alphabetCount, sep="\n", end="\n" * 2)
