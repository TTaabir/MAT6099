import pandas as pd

s = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(s, header=None)

print(df.tail())

import matplotlib.pyplot as plt
import numpy as np

# select setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', 0, 1)

# extract sepal length and petal length
X = df.iloc[0:100, [0, 2]].values

# plot data
plt.scatter(
    X[:50, 0],
    X[:50, 1],
    color='red',
    marker='o',
    label='Setosa'
)

plt.scatter(
    X[50:100, 0],
    X[50:100, 1],
    color='blue',
    marker='s',
    label='Versicolor'
)

plt.xlabel('Sepal length [cm]')
plt.ylabel('Petal length [cm]')
plt.legend(loc='upper left')
plt.show()

