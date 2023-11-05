from data import DATA


def main():
    for variable in DATA.getVariables():
        print(
            f"{variable}:",
            DATA.getAlphabet(variable=variable),
            sep="\n",
            end="\n\n",
        )
