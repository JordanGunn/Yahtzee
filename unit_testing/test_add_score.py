import unittest
from yahtzee import add_score


class TestAddScore(unittest.TestCase):

    def test_add_score_update_scorecard(self):

        test_score = 6
        test_field = "twos"
        test_player = {'NAME': 'Jordan', 'SCORECARD': {'twos': 0}}

        add_score(test_player, test_field, test_score)

        result = test_player["SCORECARD"][test_field]
        expected = 6

        self.assertEqual(result, expected)

    def test_add_score_update_scorecard_scratch(self):

        test_score = "scratch"
        test_field = "threes"
        test_player = {'NAME': 'Jordan', 'SCORECARD': {'threes': 0}}

        add_score(test_player, test_field, test_score)

        result = test_player["SCORECARD"][test_field]
        expected = "scratch"

        self.assertEqual(result, expected)
