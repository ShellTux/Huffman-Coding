from data import DATA


def main():
    for variable in DATA.getVariables():
        avgBits = DATA.averageBitsPerSymbol(variable = variable)
        lengthVariance = DATA.lengthVariance(variable = variable)

        print(
                variable,
                f'{f"Average bits per symbol:":<{24}} {avgBits:.3f}',
                f'{f"Variance of lengths:":<{24}} {lengthVariance:.3f}',
                sep = '\n',
                end = '\n' * 2
                )

    avgBits = DATA.averageBitsPerSymbol()
    lengthVariance = DATA.lengthVariance()
    print(
            'All',
            f'{f"Average bits per symbol:":<{24}} {avgBits:.3f}',
            f'{f"Variance of lengths:":<{24}} {lengthVariance:.3f}',
            sep = '\n',
            end = '\n' * 2
            )

