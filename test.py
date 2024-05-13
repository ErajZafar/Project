import random
import pandas as pd

filename = 'excel demo/demo.xlsx'
data = pd.read_excel(filename, sheet_name=None)
coordinates = data['coordinates'].values.tolist()
for c in coordinates:
    print(c[0])
