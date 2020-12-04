import unittest
from ..yahtzee import is_player_done


class TestIsPlayerDone(unittest.TestCase):

    def test_is_player_done_all_scores_filled(self):

        test_player = {"name": "Jordan", "scorecard": {"ones": 1, "twos": 2}}

        result = is_player_done(test_player)
        expected = True

        self.assertEqual(result, expected)

    def test_is_player_done_all_scores_filled_with_scratch(self):

        test_player = {"name": "Jordan", "scorecard": {"ones": 1, "twos": "scratch"}}

        result = is_player_done(test_player)
        expected = True

        self.assertEqual(result, expected)

    def test_is_player_done_scorecard_has_zeroes(self):

        test_player = {"name": "Jordan", "scorecard": {"ones": 1, "twos": 0}}

        result = is_player_done(test_player)
        expected = False

        self.assertEqual(result, expected)