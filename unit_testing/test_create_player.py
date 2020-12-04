import unittest
from ..yahtzee import create_player


class TestCreatePlayer(unittest.TestCase):

    def test_create_player_with_name(self):

        test_name = "jordan"
        test_scorecard = {"ones": 0, "twos": 0}

        result = create_player(test_name, test_scorecard)
        expected = {
            "NAME": "jordan",
            "HELD_DICE": [],
            "SCORECARD": {"ones": 0, "twos": 0}
        }

        self.assertEqual(result, expected)

    def test_create_player_multiple_not_same_address(self):

        test_name_one = "Jordan"
        test_name_two = "Nadroj"

        test_scorecard = {"ones": 0, "twos": 0}

        result_one = create_player(test_name_one, test_scorecard)
        result_two = create_player(test_name_two, test_scorecard)

        self.assertIsNot(result_one, result_two)
