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

# df.to_csv("data\\cukrzyca.csv", index=False)

X = df.iloc[:,:-1]
y = df.outcome

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame( confusion_matrix(y_test, model.predict(X_test) ) ))

print('Zmiana danych')
df1 = df.query("outcome==0").sample(n=500)
df2 = df.query("outcome==1").sample(n=500)
df3 = pd.concat([df1, df2])  # 1000 próbek

X = df3.iloc[:,:-1]
y = df3.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame( confusion_matrix(y_test, model.predict(X_test) ) ))