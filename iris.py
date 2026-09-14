import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Ch2Perceptron import Perceptron

s = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(s, header=None)

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', 0, 1)

X = df.iloc[0:100, [0, 2]].values

ppn = Perceptron(eta=0.1, n_iter=10)

ppn.fit(X, y)


if __name__ == "__main__":
    plt.plot(
        range(1, len(ppn.errors_) + 1),
        ppn.errors_,
        marker='o'
    )

    plt.xlabel('Epochs')
    plt.ylabel('Number of updates')
    plt.show()
