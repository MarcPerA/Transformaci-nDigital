# TODO
# Print result of guess_combination
# Print game over result
# Use R B Y G optionally instead of Red, Blue, Yellow Green
# Add more colors (6)
# Add unittests

import random
from functools import reduce

COLORS = ('Red', 'Blue', 'Yellow', 'Green')
TRYES = 10

POSITION_GOOD = 'Good'
POSITION_BAD = 'Bad'
POSITION_MOVED = 'Moved'

def select_random_combination(number):
    return [random.choice(COLORS) for index in range(number)]


def get_list_from_input(text_input):
    import pdb; pdb.set_trace()
    return text_input.split(', ')('Red', 'Blue', 'Yellow', 'Green')


def is_valid_input(current_combination):
    return reduce((lambda x, y: x and y in COLORS), current_combination)


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

        result.append(color, status)

    return result


def main():
    '''
        Red Blue Yellow Green  Good Bad Moved
    '''
    print('MasterMind')
    current_try = 1
    success = False

    valid_combination = select_random_combination(number=4)
    # This is for python 2, for python 3 use input
    text_input = input('Give a new combination:')

    while not current_try == TRYES and not success:
        text_input = input('Give a new combination:')
        import pdb; pdb.set_trace()
        current_combination = get_list_from_input(text_input)

        if not is_valid_input(current_combination):
            current_try += 1
            continue

        result = guess_combination(current_combination, valid_combination)

        if is_all_colors_valid(current_combination, valid_combination):
            success = True
        else:
            current_try += 1


if __name__ == '__main__':
    main()