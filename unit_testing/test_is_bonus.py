import unittest
from ..yahtzee import is_bonus


class TestIsBonus(unittest.TestCase):

    def test_is_bonus_achieved(self):

        test_player = {"name": "Jordan", "scorecard": {"upper_total": 63}}

        result = is_bonus(test_player)
        expected = True

        self.assertEqual(result, expected)

    def test_is_bonus_not_achieved(self):

        test_player = {"name": "Jordan", "scorecard": {"upper_total": 35}}

        result = is_bonus(test_player)
        expected = False

        self.assertEqual(result, expected)