from data import DATA
from data.graph import scatter
import matplotlib.pyplot as plt

def main():
    rows, cols = 3, 2
    figure, _ = plt.subplots(nrows = rows, ncols = cols)
    figure.suptitle('Ex2')
    figure.subplots_adjust(wspace=0.5, hspace=0.5)
    variables = (
            'Acceleration',
            'Cylinders',
            'Displacement',
            'Horsepower',
            'ModelYear',
            'Weight',
            )
    MPGValues = DATA.getValues(variable = 'MPG')
    for index, variable in enumerate(variables):
        # TODO: adjust subplot size according to variablePairs size
        values = DATA.getValues(variable = variable)

        scatter(
                xValues = values,
                yValues = MPGValues,
                figure  = figure,
                xLabel  = variable,
                yLabel  = 'MPG',
                subplot = int(f'{rows}{cols}{index + 1}')
                )

    plt.show()

    figure.subplots_adjust(wspace = .5, hspace = .5)
    figure.set_size_inches(rows * 4, cols * 4)
    figure.savefig('Ex2.png')

if __name__ == "__main__":
    main()
