# This is a sample Python script.
import numpy as np
import src.machine_learning.setosa_versicolor.setosaversicolor as flower_functions

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    v1 = np.array([1, 2, 3])
    v2 = 0.5 * v1
    print(np.arccos(v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))))

    flower_functions.plot_flowers()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
