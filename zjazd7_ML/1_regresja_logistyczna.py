import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv('data//diabetes.csv')
print(df.describe().T.round(2).to_string())

print('Puste wartosci')
print(df.isna().sum())

print('Co jest w outcome?')
print(df.outcome.value_counts())

# tam, gdzie zera lub brak wartości
# przypisać średnią (bez zer)

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col] = df[col].replace(0, np.nan)   # wcześniej np.NaN
    mean_ = df[col].mean()
    df[col].replace(np.nan, mean_, inplace=True)   # niedługo niewspierane
print('Po czyszczeniu danych')
print(df.describe().T.round(2).to_string())