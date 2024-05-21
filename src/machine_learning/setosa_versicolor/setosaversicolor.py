import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import src.machine_learning.perceptron.perceptron as perceptron
from matplotlib.colors import ListedColormap

from src.machine_learning import data_set
from src.machine_learning.data_set import dataset

df = pd.read_csv('https://archive.ics.uci.edu/ml/'
                 'machine-learning-databases/iris/iris.data',
                 header=None)

X, y = dataset.Data().dataset()


class SetosaVersicolor:
    data_set = dataset.Data()

    ppn = perceptron.Perceptron(eta=0.1, n_iter=10)

    # v1 = np.array([1, 2, 3])
    # v2 = 0.5 * v1
    # print(np.arccos(v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))))
    # flower_functions.plot_flowers()

    # seleccionar setosa y versicolor

    def __init__(self):
        self.errors_ = None
        self.resolution = None

    def plot_decision_regions(self, resolution=None, ppn=perceptron, data=data_set):
        self.resolution = resolution
        self.ppn = ppn
        self.data_set = data_set

        # setup marker generator and color map
        markers = ('s', 'x', 'o', '^', 'v')
        colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(data.dataset()))])

        # plot the decision surface
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                               np.arange(x2_min, x2_max, resolution))
        Z = ppn.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        Z = Z.reshape(xx1.shape)
        plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())

        # plot class examples
        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(
                x=X[y == cl, 0],
                y=X[y == cl, 1],
                alpha=0.8,
                c=colors[idx],
                marker=markers[idx],
                label=cl,

                # edgecolor='black'
            )

    def plot_flowers(ppn=None):
        # representar los datos
        plt.scatter(X[:50, 0], X[:50, 1],
                    color='red', marker='o', label='Iris-setosa')

        plt.scatter(X[50:100, 0], X[50:100, 1],
                    color='blue', marker='x', label='Iris-versicolor'),

        plt.xlabel('sepal length [cm]')
        plt.ylabel('petal length [cm]')
        plt.legend(loc='upper left')

        plt.show()

        plt.plot(range(1, len(ppn.errors_) + 1),
                 ppn.errors_, marker='o')

        plt.xlabel('Epochs')
        plt.ylabel('Number of updates')
        plt.show()

#
