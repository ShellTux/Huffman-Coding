from data import DATA
from data.graph import histogram
import matplotlib.pyplot as plt

def main():
    figure = plt.figure('Histogram')
    variable = 'Acceleration'
    alphabet, alphabetCount = DATA.getAlphabet(
            variable    = variable,
            returnCount = True
            )
    print(alphabet, alphabetCount, sep = '\n')
    histogram(
            xValues = alphabet.astype(str),
            yValues = alphabetCount,
            xLabel  = variable,
            yLabel  = 'Count',
            figure  = figure,
            )

    plt.show()

    figure.subplots_adjust(wspace = .5, hspace = .5)
    figure.savefig('Ex5.png')
