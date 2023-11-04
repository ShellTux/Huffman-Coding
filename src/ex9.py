from data import DATA

def main():
    variableX = 'MPG'
    for variableY in DATA.getVariables():
        if variableY == variableX:
            continue

        pearsonCoeficient = DATA.pearsonCoeficient(
                variableX = variableX,
                variableY = variableY,
                )
        print(f'Coeficiencia de {variableX} e {variableY}: {pearsonCoeficient}')

if __name__ == '__main__':
    main()
