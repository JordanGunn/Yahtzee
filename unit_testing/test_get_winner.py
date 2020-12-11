import unittest
from yahtzee import get_winner


class TestGetWinner(unittest.TestCase):

    def test_get_winner_two_players(self):

        test_players_done = [
            {"NAME": "Jordan", "final_score": 3},
            {"NAME": "Jordan", "final_score": 2}
        ]

        result = get_winner(test_players_done)
        expected = {"NAME": "Jordan", "final_score": 3}

        self.assertEqual(result, expected)

    def test_get_winner_one_player(self):

        test_players_done = [{"NAME": "Jordan", "final_score": 1}]

        result = get_winner(test_players_done)
        expected = {"NAME": "Jordan", "final_score": 1}

        self.assertEqual(result, expected)