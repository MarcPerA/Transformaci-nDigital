import unittest

from app import (
    select_random_combination, get_list_from_input,
    is_valid_input, is_all_colors_valid
)


class MastermindTestCase(unittest.TestCase):

    def test_random_combination_return_six_elements(self):
        # Arrange
        number = 6

        # Act
        combination_list = select_random_combination(number)

        # Assert
        self.assertEqual(len(combination_list), number)

    def test_get_list_from_input_with_one_element(self):
        input = 'Yellow'

        output = get_list_from_input(input)

        self.assertEqual(output, [input])

    def test_get_list_from_input_with_four_elements(self):
        input = 'Yellow, Blue'
        expected_output = ['Yellow', 'Blue']

        output = get_list_from_input(input)

        self.assertEqual(output, expected_output)

    def test_is_valid_input_return_true_one_element_with_letter(self):
        input = ['B']

        output = is_valid_input(input)

        self.assertTrue(output)

    def test_is_valid_input_return_true_one_element(self):
        input = ['Blue']

        output = is_valid_input(input)

        self.assertTrue(output)

    def test_is_valid_input_return_true_more_than_one_element(self):
        input = ['Blue', 'Yellow']

        output = is_valid_input(input)

        self.assertTrue(output)

    def test_is_valid_input_return_false(self):
        input = ['Purple', 'Yellow']

        output = is_valid_input(input)

        self.assertFalse(output)

    def test_is_all_colors_valid_return_true(self):
        # TODO
        pass

    def test_is_all_colors_valid_return_false(self):
        # TODO
        pass

    # TODO test guess_combination

if __name__ == '__main__':
    unittest.main()