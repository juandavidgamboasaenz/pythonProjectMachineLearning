import pandas as pd
import numpy as np

df = pd.read_csv('https://archive.ics.uci.edu/ml/'
                 'machine-learning-databases/iris/iris.data',
                 header=None)


class Data:
    def __init__(self):
        self.df = None

    def dataset(self):
        self.df = df

        df.tail()
        y = df.iloc[0:150, 4].values
        y = np.where(y == 'Iris-setosa', -1, 1)
        # extraer longitud de sépalo y longitud de pétalo
        X = df.iloc[0:, [0, 2]].values

        return X, y
