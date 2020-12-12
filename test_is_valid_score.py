import unittest
from yahtzee import is_valid_score


class TestIsValidScore(unittest.TestCase):

    def test_is_valid_score_field_filled(self):

        test_player = {"SCORECARD": {"ones": 1, "twos": 0, "yahtzee": 50}}
        test_key = "ones"
        test_score = 1

        expected = False
        result = is_valid_score(test_player, test_key, test_score)
        self.assertEqual(result, expected)

    def test_is_valid_score_no_score(self):

        test_player = {"SCORECARD": {"ones": 1, "twos": 0, "yahtzee": 50}}
        test_key = "ones"
        test_score = 0

        expected = False
        result = is_valid_score(test_player, test_key, test_score)
        self.assertEqual(result, expected)

    def test_is_valid_score_field_available(self):

        test_player = {"SCORECARD": {"ones": 0, "twos": 0, "yahtzee": 50}}
        test_key = "ones"
        test_score = 1

        expected = True
        result = is_valid_score(test_player, test_key, test_score)
        self.assertEqual(result, expected)

    def test_is_valid_score_yahtzee_field_filled(self):

        test_player = {"SCORECARD": {"ones": 0, "twos": 0, "yahtzee": 50}}
        test_key = "ones"
        test_score = 50

        expected = True
        result = is_valid_score(test_player, test_key, test_score)
        self.assertEqual(result, expected)
