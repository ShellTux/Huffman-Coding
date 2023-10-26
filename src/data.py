import numpy as np
import pandas as pd

def variableValues(values, varNames, label):
    return values[:,varNames.index(label)]

def variableAlphabet(values, varNames, label):
    return np.unique(variableValues(values.astype(np.uint16),varNames, label))

def variableAlphabetCount(values, varNames, label):
    varValues = variableValues(values, varNames, label)
    count = np.zeros(varValues.max()+1, dtype=np.uint32)
    for symbol in varValues:
        count[symbol] += 1
    count = count[count != 0]
    return count

data = pd.read_excel('./assets/CarDataset.xlsx')
varNames = data.columns.values.tolist()
values = data.values

