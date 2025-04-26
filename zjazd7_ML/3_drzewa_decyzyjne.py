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


print('Algorytm Drzewa decyzyjne')
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
X = df.iloc[:, :2]
y = df.class_value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
model = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, class_weight=None, ccp_alpha=0.0, monotonic_cst=None)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame( confusion_matrix(y_test, model.predict(X_test)  ) ))

from mlxtend.plotting import plot_decision_regions

plt.figure(figsize=(7,7))
plot_decision_regions(X.values, y.values, model)


from dtreeplt import dtreeplt

dtree = dtreeplt(model=model, feature_names=X.columns, target_names=["setosa","versicolor","virginica"])
dtree.view()
plt.show()
