import unittest
from ..yahtzee import check_number


class TestCheckNumber(unittest.TestCase):

    def test_check_number_ones(self):

        test_roll = [2, 6, 1, 3, 4]

        result = check_number(test_roll, 1)
        expected = 1

        self.assertEqual(result, expected)

    def test_check_number_sixes(self):

        test_roll = [2, 6, 1, 3, 4]

        result = check_number(test_roll, 1)
        expected = 6

        self.assertEqual(result, expected)

    def test_check_number_ones_multiple(self):

        test_roll = [2, 1, 1, 3, 4]

        result = check_number(test_roll, 1)
        expected = 2

        self.assertEqual(result, expected)

    def test_check_number_ones_all(self):

        test_roll = [1, 1, 1, 1, 1]

        result = check_number(test_roll, 1)
        expected = 2

        self.assertEqual(result, expected)
