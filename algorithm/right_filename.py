import numpy as np
import sys

# Load last made matrix
matrix = np.load('matrices/matrix.npy')

# Add the matrix to the correct matrix file
for i in sys.stdin:
    x = 'matrices/' + i.split('\n')[0][:-1] + '_matrix'
    np.save(x, matrix)
