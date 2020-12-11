import unittest
from yahtzee import is_bonus


class TestIsBonus(unittest.TestCase):

    def test_is_bonus_achieved(self):

        test_player = {"NAME": "Jordan", "SCORECARD": {"ones": 63}}

        result = is_bonus(test_player)
        expected = True

        self.assertEqual(result, expected)

    def test_is_bonus_not_achieved(self):

        test_player = {"NAME": "Jordan", "SCORECARD": {"ones": 35}}

        result = is_bonus(test_player)
        expected = False

        self.assertEqual(result, expected)

    def test_is_bonus_achieved_sum_of_scores(self):

        test_player = {"NAME": "Jordan", "SCORECARD": {"ones": 35, "twos": 35}}

        result = is_bonus(test_player)
        expected = True

        self.assertEqual(result, expected)

    def test_is_bonus_not_achieved_sum_of_scores(self):

        test_player = {"NAME": "Jordan", "SCORECARD": {"ones": 1, "twos": 2}}

        result = is_bonus(test_player)
        expected = False

        self.assertEqual(result, expected)
