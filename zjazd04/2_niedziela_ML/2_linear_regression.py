import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('data\\otodom.csv')
print(df)
print(df.describe().T.to_string())

# print(df.loc[:,'cena'])
# sns.heatmap(df.iloc[ : ,1:].corr(), annot=True)
# plt.show()
#print(df.corr())

# sns.histplot(df.cena)
# plt.show()
# plt.scatter(df.powierzchnia, df.cena)
# plt.show()

q1 = df.describe().loc['25%', 'cena']
print(q1)
q3 = df.describe().loc['75%', 'cena']
print(q3)

# df1 = df[(df.cena >= q1) & (df.cena <= q3)]
df1 = df[(df.cena <= q3)]

sns.histplot(df1.cena)
plt.show()

X = df1.iloc[: , 2:]   #wszystkie kolumny bez 2 pierwszych
y = df1.cena

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, X_test.shape)

model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

print(model.coef_)
print(pd.DataFrame(model.coef_, X.columns))

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))