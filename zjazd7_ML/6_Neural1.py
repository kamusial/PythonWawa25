import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data\\f-c.csv')
model = LinearRegression()
model.fit(df[['F']], df.C)

print(f'Wspolczynnik kierunkowy: {model.coef_}\nWyraz wolny: {model.intercept_}')
plt.scatter(df.F, df.C)
plt.plot(df.F, df.F*model.coef_ + model.intercept_, c='r')
plt.show()