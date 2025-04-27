import matplotlib.pyplot as plt
import numpy as np
from numpy.random import seed
import pandas as pd
from sklearn.datasets import load_breast_cancer
from collections import Counter
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

### Pandas - ustawienia
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 10000)
pd.set_option('display.max_colwidth', 10000)
np.set_printoptions(linewidth=2000)


X, y =load_breast_cancer(return_X_y=True, as_frame=True)
print(X.shape)
print(X.columns)
print(X.describe())
print(Counter(y))

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model = MLPClassifier(hidden_layer_sizes=(100, 100, 100, 100, 100), max_iter=1000, activation='relu')
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(pd.DataFrame(confusion_matrix(y_test, y_pred)))
# print(accuracy_score(y_test, y_pred))
# print(model.n_layers_)
score = []
kfold = RepeatedStratifiedKFold()
for train, test in kfold.split(X, y):
    model = MLPClassifier(hidden_layer_sizes=(100, 100, 100), max_iter=100, activation='relu')
    X_train, X_test = X.iloc[train, :], X.iloc[test, :]
    y_train, y_test = y.iloc[train], y.iloc[test]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score.append(accuracy_score(y_test, y_pred))
print(score)
plt.plot(score)
plt.grid()
plt.show()

import joblib
# joblib.dump(model, 'My_model.model')
zaladowany_model = joblib.load('My_model.model')


