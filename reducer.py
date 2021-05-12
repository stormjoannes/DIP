import sys
import numpy as np
import ast

totale_matrix = np.zeros((28, 28))

for matrix in sys.stdin:
    matrix = ast.literal_eval(matrix)
    totale_matrix += matrix
    totale_matrix /= 2

print(totale_matrix)