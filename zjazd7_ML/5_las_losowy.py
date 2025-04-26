import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv("data\\heart.csv", comment='#')
print(df)

X = df.iloc[: , :-1]
y = df.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
model = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=None, min_samples_split=2)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame( confusion_matrix(y_test, model.predict(X_test)  ) ))
print(pd.DataFrame( model.feature_importances_ , X.columns))