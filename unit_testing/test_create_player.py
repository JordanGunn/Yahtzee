import unittest
from yahtzee import create_player


class TestCreatePlayer(unittest.TestCase):

    def test_create_player_with_name(self):

        test_name = "jordan"

        result = create_player(test_name)

        expected = {
            "NAME": "jordan",
            "HELD_DICE": [],
            "SCORECARD": {"ones": 0, "twos": 0}
        }

        self.assertEqual(result, expected)

    def test_create_player_multiple_not_same_address(self):

        test_name_one = "Jordan"
        test_name_two = "Nadroj"

        result_one = create_player(test_name_one)
        result_two = create_player(test_name_two)

        self.assertIsNot(result_one, result_two)
