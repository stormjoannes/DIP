import numpy as np
from mapper import create_matrix, characters


def convert_to_percentage(characters, input_line):
    """"Convert all values in matrix to percentage based on part of the total."""
    matrix = create_matrix(characters, input_line)

    total = np.sum(matrix)
    for row in range(len(matrix)):
        for index in range(len(matrix)):
            matrix[row][index] = matrix[row][index] / total
    return matrix


def language_chooser(dutch_matrix, eng_matrix, test_matrix):
    """Compare given test line matrix with language matrices and return the chosen language."""
    dutch_loss = 0
    eng_loss = 0

    for row in range(len(dutch_matrix)):
        # Get percentage at current index on matrix
        for index in range(len(dutch_matrix)):
            dutch_perc = dutch_matrix[row][index]
            eng_perc = eng_matrix[row][index]
            test_perc = test_matrix[row][index]

            # Add difference from percentile from character from line to Dutch or English loss
            dutch_loss += abs(dutch_perc - test_perc)
            eng_loss += abs(eng_perc - test_perc)

    # The language with lowest loss has least difference with sentence structure and is chosen
    return "dutch" if dutch_loss < eng_loss else "english"


def text_scanner(input_text, dutch_matrix, eng_matrix, characters):
    """Loop thru all lines and sum the amount a language is chosen for a result."""
    dutch_count = 0
    eng_count = 0

    for test_input_line in input_text:
        test_matrix = convert_to_percentage(characters, test_input_line)
        result = language_chooser(dutch_matrix, eng_matrix, test_matrix)

        if result == "dutch":
            dutch_count += 1
        else:
            eng_count += 1
    return dutch_count, eng_count


# Load Dutch and English matrix and load input_text
Dutch_matrix = np.load('matrices/Dutch_matrix.npy')
English_matrix = np.load('matrices/English_matrix.npy')
input_text = open('data/test_file.txt', encoding='utf8')

result = text_scanner(input_text, Dutch_matrix, English_matrix, characters)

# Print formatted results
expected_result = (73, 119)
accuracy = 100 - (abs(result[1] - expected_result[1]) / sum(expected_result) * 100)
print(f'Result: \nDutch sentences: {result[0]} \nEnglish sentences: {result[1]}\n')
print(f'Expected result = Dutch sentences: {expected_result[0]}, English sentences: {expected_result[1]}')
print('Accuracy: ' + str(accuracy) + '%')
