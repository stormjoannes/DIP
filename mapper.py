import numpy as np
import sys

characters = 'abcdefghijklmnopqrstuvwxyz '

def create_matrix(characters, line):
    matrix = np.zeros((len(characters) + 1, len(characters) + 1))

    for i in range(0, len(line) - 1):
        letter = line[i].lower()
        opvolgende_letter = line[i + 1].lower()

        if letter in characters:
            index_letter = characters.index(letter)
        else:
            index_letter = 27

        if opvolgende_letter in characters:
            index_opvolgende_letter = characters.index(opvolgende_letter)
        else:
            index_opvolgende_letter = 27

        matrix[index_letter][index_opvolgende_letter] += 1
    return matrix


for line in sys.stdin:
    matrix = create_matrix(characters, line)

    print(matrix.tolist())