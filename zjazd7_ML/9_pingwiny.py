import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')
# print(type(penguins))
# print(penguins.head().to_string())
# sns.pairplot(penguins, hue='species')
# plt.show()

penguins_filtered = penguins.drop(columns=['island', 'sex']).dropna()
print(penguins_filtered.head().to_string())
penguins_features = penguins_filtered.drop(columns=['species'])
penguins_target = pd.get_dummies(penguins_filtered['species'])
print(penguins_target)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(penguins_features, penguins_target, test_size=0.2)


