import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(1, activation='linear'))
model.add(Dense(20, activation='relu'))
model.add(Dense(14, activation='linear'))
# model.add(Dense(4, activation='linear'))
model.add(Dense(1, activation='linear'))
# liczba warstw, liczna neuronów w warstwie
# funkcja aktywacji
model.compile(optimizer='rmsprop', loss='mse')

df = pd.read_csv('data\\f-c.csv', usecols=[1, 2])

result = model.fit(df.F, df.C, epochs=400, verbose=2)
# liczba epok

C_pred = model.predict(df.F)
plt.scatter(df.F, df.C)
plt.plot(df.F, C_pred, c='r')
plt.show()
