import numpy as np
import pandas as pd
def variableValues(values, varNames, label):
    return values[:,varNames.index(label)]
def variableAlphabet(values, varNames, label):
    return np.unique(variableValues(values.astype(np.uint16),varNames, label))
data = pd.read_excel('./assets/CarDataset.xlsx')
varNames = data.columns.values.tolist()
values = data.values