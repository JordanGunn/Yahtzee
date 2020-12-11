import unittest
from yahtzee import check_number


class TestCheckNumber(unittest.TestCase):

    def test_check_number_ones(self):

        test_roll = [1, 2, 4, 5, 6]

        result = check_number(test_roll, 1)
        expected = 1

        self.assertEqual(result, expected)

    def test_check_number_sixes(self):

        test_roll = [1, 2, 3, 4, 5]

        result = check_number(test_roll, 1)
        expected = 1

        self.assertEqual(result, expected)

    def test_check_number_ones_multiple(self):

        test_roll = [1, 1, 2, 3, 4]

        result = check_number(test_roll, 1)
        expected = 2

        self.assertEqual(result, expected)

    def test_check_number_ones_all(self):

        test_roll = [1, 1, 1, 1, 1]

        result = check_number(test_roll, 1)
        expected = 5

        self.assertEqual(result, expected)

    def test_check_number_ones_no_ones(self):

        test_roll = [6, 6, 6, 6, 6]

        result = check_number(test_roll, 1)
        expected = 0

        self.assertEqual(result, expected)
