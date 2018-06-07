# TODO
# TEST for guess_combination
# Fix failing test
# Add more colors (6)


import random
from functools import reduce

COLORS = ('Red', 'Blue', 'Yellow', 'Green')
COLOR_LETTERS = [item[0] for item in COLORS]
TRYES = 10

result = []
POSITION_GOOD = 'Good'
POSITION_BAD = 'Bad'
POSITION_MOVED = 'Moved'
LIMIT_TRIES = 5

def select_random_combination(number):
    return [random.choice(COLOR_LETTERS) for index in range(number)]


def get_list_from_input(text_input):
    return text_input.split(' ')


def is_valid_input(current_combination):
    valid = True

    for item in current_combination:
        if item not in COLORS and item not in COLOR_LETTERS:
            return False

    return valid


def is_all_colors_valid(current_combination, valid_combination):
    return current_combination == valid_combination


def guess_combination(current_combination, valid_combination):
    ''' suponemos que las dos listas tienen los mismos elementos '''
    result = []
    status = POSITION_BAD

    for index, color in enumerate(current_combination):

        if valid_combination[index] == color:
            status = POSITION_GOOD
        elif color in valid_combination:
            status = POSITION_MOVED

        result.append((color, status))

    return result


def print_combination(current_combination_result):
    for item in current_combination_result:
        print('{} status: {}'.format(item[0], item[1]))


def main():
    '''
        Red Blue Yellow Green  Good Bad Moved
    '''
    print('MasterMind')
    current_try = 1

    valid_combination = select_random_combination(number=4)

    while not current_try == TRYES:
        text_input = input('Give a new combination:\n')
        current_combination = get_list_from_input(text_input)

        if not is_valid_input(current_combination):
            current_try += 1
            continue

        result = guess_combination(current_combination, valid_combination)
        print_combination(result)

        if is_all_colors_valid(current_combination, valid_combination):
            print('Congratulations!')
            return
        else:
            current_try += 1

        if current_try == LIMIT_TRIES:
            print('GAME OVER!')
            return


if __name__ == '__main__':
    main()