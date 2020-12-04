import unittest
from ..yahtzee import get_final_score


class TestGetFinalScore(unittest.TestCase):

    def test_get_final_score_all_scores_filled(self):

        test_player = {"name": "Jordan", "scorecard": {"ones": 1, "twos": 2}}

        result = get_final_score(test_player)
        expected = {"name": "Jordan", "final_score": 3}

        self.assertEqual(result, expected)

    def test_get_final_score_scores_filled_with_scratch(self):

        test_player = {"name": "Jordan", "scorecard": {"ones": 1, "twos": "scratch"}}

        result = get_final_score(test_player)
        expected = {"name": "Jordan", "final_score": 1}

        self.assertEqual(result, expected)

    def test_get_final_score_scores_all_scratch(self):

        test_player = {"name": "Jordan", "scorecard": {"ones": "scratch", "twos": "scratch"}}

        result = get_final_score(test_player)
        expected = {"name": "Jordan", "final_score": 0}

        self.assertEqual(result, expected)
