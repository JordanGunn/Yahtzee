import unittest
from ..yahtzee import add_score


class TestAddScore(unittest.TestCase):

    def test_add_score_update_scorecard(self):

        test_score = 6
        test_field = "twos"
        test_player = {'name': 'Jordan', 'scorecard': {'twos': 0}}

        add_score(test_player, test_field, test_score)

        result = test_player["scorecard"][test_field]
        expected = 6

        self.assertEqual(result, expected)

    def test_add_score_update_scorecard_scratch(self):

        test_score = "scratch"
        test_field = "threes"
        test_player = {'name': 'Jordan', 'scorecard': {'threes': 0}}

        add_score(test_player, test_field, test_score)

        result = test_player["scorecard"][test_field]
        expected = "scratch"

        self.assertEqual(result, expected)
