import unittest
from yahtzee import get_final_score


class TestGetFinalScore(unittest.TestCase):

    def test_get_final_score_all_scores_filled(self):

        test_player = {"NAME": "Jordan", "SCORECARD": {"ones": 1, "twos": 2}}

        result = get_final_score(test_player)
        expected = {"NAME": "Jordan", "final_score": 3}

        self.assertEqual(result, expected)

    def test_get_final_score_scores_filled_with_scratch(self):

        test_player = {"NAME": "Jordan", "SCORECARD": {"ones": 1, "twos": "scratch"}}

        result = get_final_score(test_player)
        expected = {"NAME": "Jordan", "final_score": 1}

        self.assertEqual(result, expected)
