import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data\\iris.csv")
print(df['class'].value_counts())

species = {
    'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2
}

df['class_value'] = df['class'].map(species)
print(df['class_value'].value_counts())
sample = [5.6, 3.2, 5.2, 1.45]

# plt.scatter(df.sepallength, df.sepalwidth)
sns.scatterplot(df, x='sepallength', y='sepalwidth', hue='class')
plt.scatter(5.6, 3.2, c='r')
plt.show()
sns.scatterplot(df, x='petallength', y='petalwidth', hue='class')
plt.scatter(5.2, 1.45, c='r')
plt.show()

# obliczać dystans pomiędzy próbką a istniejącymi danymi
df["distance"] = (df.sepallength-sample[0])**2 + (df.sepalwidth-sample[1])**2 +\
                 (df.petallength-sample[2])**2 + (df.petalwidth-sample[3])**2

print(df.head(5).to_string())
print(df.sort_values('distance').head(7).to_string())