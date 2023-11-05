from data import DATA


def main():
    variables = DATA.getVariables()
    maxVariableLength = max(map(len, variables))
    for variable in variables:
        bps = DATA.bitsPerSymbol(variable=variable)
        print(f"{variable:<{maxVariableLength}} = {bps:.2f} bits/symbol")

    print()

    # All values
    valuesBPS = DATA.bitsPerSymbol()
    print(f"bps(values) = {valuesBPS:.2f} bits/symbol")
