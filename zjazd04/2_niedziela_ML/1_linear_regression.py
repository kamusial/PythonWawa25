import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('weight-height.csv')
print(df)
print(df.head(10))

df.Height *= 2.54
df.Weight /= 2.2
print(df.describe())

# plt.hist(df.Weight)
# plt.show()
# plt.hist(df.query("Gender=='Male'").Weight, bins=30)
# plt.hist(df.query("Gender=='Female'").Weight, bins=30)
# plt.show()
# sns.histplot(df.Weight)
# plt.show()
# sns.histplot(df.query("Gender=='Male'").Weight)
# sns.histplot(df.query("Gender=='Female'").Weight)
# plt.show()

# wejściowe, dane niezależne -> gender, height
# wyjście, dane zaleźne -> weight

df = pd.get_dummies(df)
print(df)
del (df['Gender_Male'])
print(df)
