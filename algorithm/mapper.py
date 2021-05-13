import sys
import numpy as np


def create_matrix(characters, line):
    """"Create a matrix for each letter in the alfabet from the given line."""
    # Make empty matrix
    matrix = np.zeros((len(characters) + 1, len(characters) + 1))

    # Loop thru all characters in the given line and fill the matrix
    for i in range(0, len(line) - 1):
        letter = line[i].lower()
        following_character = line[i + 1].lower()

        if letter in characters:
            index_character = characters.index(letter)
        else:
            index_character = 27

        if following_character in characters:
            index_following_character = characters.index(following_character)
        else:
            index_following_character = 27

        matrix[index_character][index_following_character] += 1
    return matrix


characters = 'abcdefghijklmnopqrstuvwxyz '

# Don't run this if file is imported
if __name__ == "__main__":
    for line in sys.stdin:
        matrix = create_matrix(characters, line)
        print(matrix.tolist())
