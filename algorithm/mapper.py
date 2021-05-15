import sys
from General_definitions import create_matrix


# All characters where our matrix consists of
characters = 'abcdefghijklmnopqrstuvwxyz '

# Don't run this if file is imported
if __name__ == "__main__":
    # Loop through all lines in file and create a matrix for each line
    for line in sys.stdin:
        matrix = create_matrix(characters, line)
        print(matrix.tolist())