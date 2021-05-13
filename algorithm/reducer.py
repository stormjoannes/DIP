import sys
import numpy as np
import ast


def reduce():
    """"Loop thru text files and add all matrices to each other. this way you get a matrix that represents a language"""
    total_matrix = np.zeros((28, 28))

    for matrix in sys.stdin:
        matrix = ast.literal_eval(matrix)
        total_matrix += matrix

    total = np.sum(total_matrix)
    for row in range(len(total_matrix)):
        for index in range(len(total_matrix)):
            total_matrix[row][index] = total_matrix[row][index] / total

    np.save('matrices/matrix', total_matrix)


reduce()
