import sys
import numpy as np
import ast


totale_matrix = np.zeros((28, 28))

for matrix in sys.stdin:
    matrix = ast.literal_eval(matrix)
    totale_matrix += matrix

total = np.sum(totale_matrix)
for row in range(len(totale_matrix)):
    for index in range(len(totale_matrix)):
        totale_matrix[row][index] = totale_matrix[row][index] / total

np.save('matrices/English_matrix', totale_matrix)

