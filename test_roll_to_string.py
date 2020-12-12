import unittest
from yahtzee import roll_to_string


class TestRollToString(unittest.TestCase):

    def test_roll_to_string_one_number(self):

        test_roll = [5]

        expected = '5'
        result = roll_to_string(test_roll)
        self.assertEqual(result, expected)

    def test_roll_to_string_multiple_numbers(self):

        test_roll = [5, 5, 5]

        expected = '555'
        result = roll_to_string(test_roll)
        self.assertEqual(result, expected)


