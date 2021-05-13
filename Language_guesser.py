import numpy as np


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


def convert_to_percentage(characters, input_line):
    matrix = create_matrix(characters, input_line)

    total = np.sum(matrix)
    for row in range(len(matrix)):
        for index in range(len(matrix)):
            matrix[row][index] = matrix[row][index] / total
    return matrix


def language_chooser(dutch_matrix, eng_matrix, test_matrix):
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

        result = language_chooser(dutch_matrix, eng_matrix, test_matrix)

        if result == "dutch":
            dutch_count += 1
        else:
            eng_count += 1
    return dutch_count, eng_count


Dutch_matrix = np.load('matrixes/Dutch_matrix.npy')
English_matrix = np.load('matrixes/English_matrix.npy')
input_text = open('data/test_file.txt', encoding='utf8')

characters = 'abcdefghijklmnopqrstuvwxyz '

result = text_scanner(input_text, Dutch_matrix, English_matrix, characters)
expected_result = (73, 119)
accuracy = 100 - (abs(result[1] - expected_result[1]) / sum(expected_result) * 100)
print(f'Result: \nDutch sentences: {result[0]} \nEnglish sentences: {result[1]}\n')
print(f'Expected result = Dutch sentences: {expected_result[0]}, English sentences: {expected_result[1]}')
print('Accuracy: ' + str(accuracy) + '%')
