import numpy as np
import sys

matrix = np.load('matrices/matrix.npy')

for i in sys.stdin:
    x = 'matrices/' + i.split('\n')[0][:-1] + '_matrix'
    np.save(x, matrix)