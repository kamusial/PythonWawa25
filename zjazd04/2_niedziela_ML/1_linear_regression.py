import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
print(df.head(10))

df.Height *= 2.54
df.Weight /= 2.2
print(df.describe())