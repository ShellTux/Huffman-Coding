from data import DATA


def main():
    MI = DATA.mutualInformation(
            variableX = 'MPG',
            variableY = 'Weight',
            )
    print(MI)

if __name__ == "__main__":
    main()
