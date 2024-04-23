# This is a sample Python script.
import numpy as np
import src.machine_learning.setosa_versicolor.setosaversicolor as flower_functions

# Press shift + F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import src.practie_question.PracticeQuestion
from src.practie_question import PracticeQuestion


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(("55" > "100"))
    queries = [["ADD", "0"],
               ["ADD", "1"],
               ["ADD", "1"],
               ["ADD", "11"],
               ["ADD", "22"],
               ["ADD", "3"],
               ["ADD", "5"],
               ["GET_NEXT", "0"],
               ["GET_NEXT", "1"],
               ["REMOVE", "1"],
               ["GET_NEXT", "1"],
               ["ADD", "0"],
               ["ADD", "1"],
               ["ADD", "2"],
               ["ADD", "1"],
               ["GET_NEXT", "1"],
               ["GET_NEXT", "2"],
               ["GET_NEXT", "3"],
               ["GET_NEXT", "5"]]
    PracticeQuestion.solution(queries)
