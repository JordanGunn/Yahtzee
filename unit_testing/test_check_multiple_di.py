import unittest
from ..yahtzee import check_multiple_di


class TestCheckMultipleDi(unittest.TestCase):

    def test_check_multiple_di_with_multiple_di(self):

        test_roll = [6, 6, 6, 2, 1]
        test_value = 3

        result = check_multiple_di(test_roll, test_value)
        expected = 21

        self.assertEqual(result, expected)

    def test_check_multiple_di_two_groups_of_repetition_get_smaller(self):

        test_roll = [6, 6, 6, 2, 2]
        test_repetition = 2

        result = check_multiple_di(test_roll, test_repetition)
        expected = 21

        self.assertEqual(result, expected)

    def test_check_multiple_di_two_groups_of_repetition_get_larger(self):

        test_roll = [6, 6, 6, 2, 2]
        test_repetition = 3

        result = check_multiple_di(test_roll, test_repetition)
        expected = 22

        self.assertEqual(result, expected)

    def test_check_multiple_di_all_same_number(self):

        test_roll = [6, 6, 6, 6, 6]
        test_repetition = 5

        result = check_multiple_di(test_roll, test_repetition)
        expected = 50

        self.assertEqual(result, expected)

    def test_check_multiple_di_no_repetition(self):

        test_roll = [1, 2, 3, 4, 5]
        test_repetition = 5

        result = check_multiple_di(test_roll, test_repetition)
        expected = 0

        self.assertEqual(result, expected)
