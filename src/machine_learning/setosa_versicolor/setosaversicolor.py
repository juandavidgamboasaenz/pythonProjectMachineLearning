import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import src.machine_learning.perceptron.Perceptron as perceptron


# v1 = np.array([1, 2, 3])
# v2 = 0.5 * v1
# print(np.arccos(v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))))
# flower_functions.plot_flowers()

# seleccionar setosa y versicolor
def plot_flowers():
    df = pd.read_csv('https://archive.ics.uci.edu/ml/'
                     'machine-learning-databases/iris/iris.data',
                     header=None)
    df.tail()

    y = df.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)

    # extraer longitud de sépalo y longitud de pétalo
    x = df.iloc[0:100, [0, 2]].values

    # representar los datos
    plt.scatter(x[:50, 0], x[:50, 1],
                color='red', marker='o', label='Iris-setosa')

    plt.scatter(x[50:100, 0], x[50:100, 1],
                color='blue', marker='x', label='Iris-versicolor'),

    plt.xlabel('sepal length [cm]')
    plt.ylabel('petal length [cm]')
    plt.legend(loc='upper left')

    plt.show()

    ppn = perceptron.Perceptron(eta=0.1, n_iter=10)
    ppn.fit(x, y)
    plt.plot(range(1, len(ppn.errors_) + 1),
             ppn.errors_, marker='o')

    plt.xlabel('Epochs')
    plt.ylabel('Number of updates')
    plt.show()
