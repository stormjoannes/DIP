import numpy as np
import sys

alle_dingen = 'abcdefghijklmnopqrstuvwxyz '

for line in sys.stdin:
    zeros = np.zeros((len(alle_dingen) + 1, len(alle_dingen) + 1))

    for i in range(0, len(line) - 1):
        letter = line[i].lower()
        opvolgende_letter = line[i + 1].lower()

        if letter in alle_dingen:
            index_letter = alle_dingen.index(letter)
        else:
            index_letter = 27

        if opvolgende_letter in alle_dingen:
            index_opvolgende_letter = alle_dingen.index(opvolgende_letter)
        else:
            index_opvolgende_letter = 27

        zeros[index_letter][index_opvolgende_letter] += 1

    print(zeros.tolist())