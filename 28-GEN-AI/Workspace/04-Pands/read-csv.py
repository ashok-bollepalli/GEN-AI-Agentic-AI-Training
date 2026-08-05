import pandas as pd

df = pd.read_csv("students.csv")

print(df)
print("--------------------------")
print(df.info())
print("--------------------------")
print(df.shape)
print(df.columns)
print(df.dtypes)
print("--------------------------")
print(df.describe())