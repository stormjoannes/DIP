import sys
import numpy as np
import ast
from General_definitions import convert_to_percentage


def reduce():
    """"Loop through text files and add all matrices to each other. this way you get a matrix that represents a language"""
    total_matrix = np.zeros((28, 28))

    # Loop through all matrices
    for matrix in sys.stdin:
        matrix = ast.literal_eval(matrix)
        total_matrix += matrix

    total_matrix = convert_to_percentage(total_matrix)

    np.save('matrices/matrix', total_matrix)


reduce()
