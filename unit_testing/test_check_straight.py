import unittest
from ..yahtzee import check_straight


class TestCheckStraight(unittest.TestCase):

    def test_check_straight_large_one_to_five(self):

        test_roll = [1, 2, 3, 4, 5]

        result = check_straight(test_roll, size='large')
        expected = 40

        self.assertEqual(result, expected)

    def test_check_straight_large_two_to_six(self):

        test_roll = [2, 3, 4, 5, 6]

        result = check_straight(test_roll, size='large')
        expected = 40

        self.assertEqual(result, expected)

    def test_check_straight_large_reversed(self):

        test_roll = [5, 4, 3, 2, 1]

        result = check_straight(test_roll, size='large')
        expected = 40

        self.assertEqual(result, expected)

    def test_check_straight_large_not_sorted(self):

        test_roll = [3, 6, 2, 4, 5]

        result = check_straight(test_roll, size='large')
        expected = 40

        self.assertEqual(result, expected)

    def test_check_straight_small_with_additional_number(self):

        test_roll = [1, 2, 3, 4, 6]

        result = check_straight(test_roll, size='small')
        expected = 30

        self.assertEqual(result, expected)

    def test_check_straight_small_within_large_straight(self):

        test_roll = [1, 2, 3, 4, 5]

        result = check_straight(test_roll, size='small')
        expected = 30

        self.assertEqual(result, expected)

    def test_check_straight_small_reversed(self):

        test_roll = [4, 3, 2, 1, 6]

        result = check_straight(test_roll, size='small')
        expected = 30

        self.assertEqual(result, expected)

    def test_check_straight_small_not_sorted(self):

        test_roll = [2, 6, 1, 3, 4]

        result = check_straight(test_roll, size='small')
        expected = 30

        self.assertEqual(result, expected)



