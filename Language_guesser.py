from DIP.tweede_opdracht.mapper import create_matrix
import numpy as np


def convert_to_percentage(characters, input_line):
    matrix = create_matrix(characters, input_line)

    total = np.sum(matrix)
    for row in range(len(matrix)):
        for index in range(len(matrix)):
            matrix[row][index] = matrix[row][index] / total
    return matrix


def language_choser(dutch_matrix, eng_matrix, test_matrix):
    dutch_loss = 0
    eng_loss = 0

    for row in range(len(dutch_matrix)):
        for index in range(len(dutch_matrix)):
            dutch_perc = dutch_matrix[row][index]
            eng_perc = eng_matrix[row][index]
            test_perc = test_matrix[row][index]

            dutch_loss += abs(dutch_perc - test_perc)
            eng_loss += abs(eng_perc - test_perc)

    return "dutch" if dutch_loss < eng_loss else "english"


def text_scanner(input_text, dutch_matrix, eng_matrix, characters):
    dutch_count = 0
    eng_count = 0

    for test_input_line in input_text:
        test_matrix = convert_to_percentage(characters, test_input_line)

        result = language_choser(dutch_matrix, eng_matrix, test_matrix)

        if result == "dutch":
            dutch_count += 1
        else:
            eng_count += 1

    return dutch_count, eng_count


result = text_scanner(input_text, dutch_matrix, eng_matrix, characters)
print(result)
expected_result = (73, 119)
accuracy = 100 - (abs(result[1] - expected_result[1]) / sum(expected_result) * 100)
print(accuracy)