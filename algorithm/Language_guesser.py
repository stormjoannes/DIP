import numpy as np
from General_definitions import create_matrix
from General_definitions import convert_to_percentage


def language_chooser(first_matrix, second_matrix, test_matrix):
    """Compare given test line matrix with language matrices and return the chosen language."""
    first_matrix_loss = 0
    second_matrix_loss = 0

    for row in range(len(first_matrix)):
        # Get percentage at current index on matrix
        for index in range(len(first_matrix)):
            first_matrix_perc = first_matrix[row][index]
            second_matrix_perc = second_matrix[row][index]
            test_matrix_perc = test_matrix[row][index]

            # Calculate the difference in percentage for each spot in the matrices for each matrix
            first_matrix_loss += abs(first_matrix_perc - test_matrix_perc)
            second_matrix_loss += abs(second_matrix_perc - test_matrix_perc)

    # The language with the lowest loss has the least difference in sentence structure and is therefore chosen
    return 'first' if first_matrix_loss < second_matrix_loss else "second"


def text_scanner(input_text, first_matrix, second_matrix, characters):
    """Loop through all lines and sum the amount a language is chosen for a result."""
    first_matrix_count = 0
    second_matrix_count = 0

    for test_input_line in input_text:
        test_matrix = create_matrix(characters, test_input_line)
        test_matrix = convert_to_percentage(test_matrix)
        result = language_chooser(first_matrix, second_matrix, test_matrix)

        if result == "first":
            first_matrix_count += 1
        else:
            second_matrix_count += 1
    return first_matrix_count, second_matrix_count


def main():
    """Load all necessary text files and calculate the accuracy, print the results in a good format"""
    # Load the two matrices matrix we want to compare with and the test file
    first_matrix = np.load('matrices/Dutch_matrix.npy')
    second_matrix = np.load('matrices/English_matrix.npy')
    input_text = open('data/test_file.txt', encoding='utf8')

    characters = 'abcdefghijklmnopqrstuvwxyz '

    result = text_scanner(input_text, first_matrix, second_matrix, characters)

    # Print formatted results
    expected_result = (73, 119)
    accuracy = 100 - (abs(result[1] - expected_result[1]) / sum(expected_result) * 100)
    print(f'Result: \nDutch sentences: {result[0]} \nEnglish sentences: {result[1]}\n')
    print(f'Expected result = Dutch sentences: {expected_result[0]}, English sentences: {expected_result[1]}')
    print('Accuracy: ' + str(accuracy) + '%')


main()

