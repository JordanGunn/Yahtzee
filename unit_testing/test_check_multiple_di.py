import unittest
from yahtzee import check_multiple_die


class TestCheckMultipleDie(unittest.TestCase):

    def test_check_multiple_die_with_multiple_di(self):

        test_roll = [1, 2, 6, 6, 6]
        test_value = 3

        result = check_multiple_die(test_roll, test_value)
        expected = 21

        self.assertEqual(result, expected)

    def test_check_multiple_die_two_groups_of_repetition(self):

        test_roll = [2, 2, 6, 6, 6]
        test_repetition = 3

        result = check_multiple_die(test_roll, test_repetition)
        expected = 22

        self.assertEqual(result, expected)

    def test_check_multiple_die_all_same_number(self):

        test_roll = [6, 6, 6, 6, 6]
        test_repetition = 5

        result = check_multiple_die(test_roll, test_repetition)
        expected = 50

        self.assertEqual(result, expected)

    def test_check_multiple_die_no_repetition(self):

        test_roll = [1, 2, 3, 4, 5]
        test_repetition = 5

        result = check_multiple_die(test_roll, test_repetition)
        expected = 0

        self.assertEqual(result, expected)
