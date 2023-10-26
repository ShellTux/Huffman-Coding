import pandas as pd
from numpy import ndarray

data = pd.read_excel('./assets/CarDataset.xlsx')
varNames: list[str] = data.columns.values.tolist()
values = data.values

def variableValues(
        values: ndarray,
        varNames: list[str],
        *,
        label: str,
        ) -> ndarray:
    return values[:, varNames.index(label)]
