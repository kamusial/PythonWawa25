import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data\\otodom.csv')
print(df)
print(df.describe().T.to_string())