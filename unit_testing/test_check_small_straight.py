import unittest
from yahtzee import check_small_straight


class TestCheckSmallStraight(unittest.TestCase):

    def test_check_small_straight_with_additional_number(self):
        test_roll = [1, 2, 3, 4, 6]

        result = check_small_straight(test_roll)
        expected = 30

        self.assertEqual(result, expected)

    def test_check_small_straight_within_large_straight(self):
        test_roll = [1, 2, 3, 4, 5]

        result = check_small_straight(test_roll)
        expected = 30

        self.assertEqual(result, expected)

    def test_check_large_straight_no_straight(self):

        test_roll = [2, 2, 2, 3, 3]

        result = check_small_straight(test_roll)
        expected = 0

        self.assertEqual(result, expected)
