import sys
from General_definitions import create_matrix


characters = 'abcdefghijklmnopqrstuvwxyz '

# Don't run this if file is imported
if __name__ == "__main__":
    for line in sys.stdin:
        matrix = create_matrix(characters, line)
        print(matrix.tolist())