from data import DATA


def main():
    variables = (
        ("Weight", "MPG"),
        ("Displacement", "MPG"),
        ("Horsepower", "MPG"),
    )

    for variableX, variableY in variables:
        MI = DATA.mutualInformation(
            variableX=variableX,
            variableY=variableY,
        )
        print(f"Mutual Information ({variableX}, {variableY}) = {MI}")


if __name__ == "__main__":
    main()
