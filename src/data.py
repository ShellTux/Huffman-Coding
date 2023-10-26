import pandas as pd

data = pd.read_excel('./assets/CarDataset.xlsx')
varNames: list[str] = data.columns.values.tolist()
values = data.values
