import pandas as pd

# dataset load
data = pd.read_csv("URLdata.csv", encoding="latin1")

print(data.head())