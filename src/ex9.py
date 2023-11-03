from data import DATA

def main():
    varNames = DATA.getVariables()
    varValues = DATA.getValues()
    for index in range(varValues.shape[1] - 1):
        print(f"Coeficiencia de {varNames[6]} e {varNames[index]}: {DATA.pearsonCoeficient(varValues[:, 6], varValues[:,index])}")

if __name__ == "__main__":
    main()