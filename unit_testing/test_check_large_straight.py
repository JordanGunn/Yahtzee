import unittest
from yahtzee import check_large_straight


class TestCheckLargeStraight(unittest.TestCase):

    def test_check_large_straight_one_to_five(self):

        test_roll = [1, 2, 3, 4, 5]

        result = check_large_straight(test_roll)
        expected = 40

        self.assertEqual(result, expected)

    def test_check_large_straight_two_to_six(self):

        test_roll = [2, 3, 4, 5, 6]

        result = check_large_straight(test_roll)
        expected = 40

        self.assertEqual(result, expected)

    def test_check_large_straight_no_straight(self):

        test_roll = [2, 2, 2, 3, 3]

        result = check_large_straight(test_roll)
        expected = 0

        self.assertEqual(result, expected)


