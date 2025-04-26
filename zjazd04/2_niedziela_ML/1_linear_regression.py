import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data//weight-height.csv')
print(df)
print(df.head(10))

df.Height *= 2.54
df.Weight /= 2.2
print(df.describe())

plt.hist(df.Weight)
plt.show()
plt.hist(df.query("Gender=='Male'").Weight, bins=30)
plt.hist(df.query("Gender=='Female'").Weight, bins=30)
plt.show()
sns.histplot(df.Weight)
plt.show()
sns.histplot(df.query("Gender=='Male'").Weight)
sns.histplot(df.query("Gender=='Female'").Weight)
plt.show()

# wejściowe, dane niezależne -> gender, height
# wyjście, dane zaleźne -> weight
print('get_dummies - zamieniam dane nienumeryczne na numeryczne')
df = pd.get_dummies(df)
print(df)
print('usuwam kolumnę Gender_Male')
del (df['Gender_Male'])
print(df)
print('Zmieniam nazwę kolumny')
df.rename(columns={'Gender_Female': 'Gender'}, inplace=True)
print(df)
print('Dane gotowe')
# gender 0 - facet, 1 - kobieta

model = LinearRegression()
model.fit( df[['Height', 'Gender']]   ,  df['Weight']  )
print(f'Wspóczynnik kierunkowy: {model.coef_}\nwyraz wolny: {model.intercept_}')

height = 192
gender = 1
weight = 1.06 * height -8.8 * gender - 102.5
print(weight)

print(model.predict([[192, 0], [167, 1], [10, 1]]))