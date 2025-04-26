import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data//diabetes.csv')
print(df.describe().T.round(2).to_string())

print('Puste wartosci')
print(df.isna().sum())

print('Co jest w outcome?')
print(df.outcome.value_counts())