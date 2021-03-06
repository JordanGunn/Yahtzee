import unittest
from yahtzee import submit_score


class TestSubmitScore(unittest.TestCase):

    def test_submit_score_update_scorecard(self):

        test_available_scores = {"twos": 2}
        test_field = "twos"
        test_player = {'NAME': 'Jordan', 'SCORECARD': {'twos': 0}}

        submit_score(test_player, test_field, test_available_scores)

        result = test_player["SCORECARD"][test_field]
        expected = 2

        self.assertEqual(result, expected)

    def test_submit_score_update_scorecard_scratch(self):

        test_available_scores = {"threes": "scratch"}
        test_field = "threes"
        test_player = {'NAME': 'Jordan', 'SCORECARD': {'threes': 0}}

        submit_score(test_player, test_field, test_available_scores)

        result = test_player["SCORECARD"][test_field]
        expected = "scratch"

        self.assertEqual(result, expected)
