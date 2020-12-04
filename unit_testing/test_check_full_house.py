import unittest
from ..yahtzee import check_full_house


class TestCheckFullHouse(unittest.TestCase):

    def test_check_full_house_two_then_three(self):

        test_roll = [4, 4, 6, 6, 6]

        result = check_full_house(test_roll)
        expected = 25

        self.assertEqual(result, expected)

    def test_check_full_house_three_then_two(self):

        test_roll = [4, 4, 4, 6, 6]

        result = check_full_house(test_roll)
        expected = 25

        self.assertEqual(result, expected)

    def test_check_full_house_no_full_house(self):

        test_roll = [1, 2, 3, 4, 5]

        result = check_full_house(test_roll)
        expected = 0

        self.assertEqual(result, expected)

