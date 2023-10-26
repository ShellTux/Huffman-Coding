#!/usr/bin/env python3

import pandas as pd

if __name__ != "__main__":
    exit(0)

data = pd.read_excel('./assets/CarDataset.xlsx')
varNames = data.columns.values.tolist()
values = data.values
