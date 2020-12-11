import unittest
from yahtzee import pluck_dice


class TestPluckDice(unittest.TestCase):

    def test_pluck_dice_empty_held_dice(self):

        test_roll = [1, 1, 3, 3, 4]
        test_desired_dice = "1 1 3"
        test_player = {"NAME": "Jordan", "HELD_DICE": []}

        pluck_dice(test_player, test_roll, test_desired_dice)
        result = test_player["HELD_DICE"]
        expected = [1, 1, 3]

        self.assertEqual(result, expected)

    def test_pluck_dice_add_to_held_dice(self):

        test_roll = [3, 4]
        test_desired_dice = "4"
        test_player = {"NAME": "Jordan", "HELD_DICE": [1, 1, 3]}

        pluck_dice(test_player, test_roll, test_desired_dice)
        result = test_player["HELD_DICE"]
        expected = [1, 1, 3, 4]

        self.assertEqual(result, expected)

    def test_pluck_dice_all_dice(self):

        test_roll = [1, 1, 3, 3, 4]
        test_desired_dice = "4 3 1 1 3"
        test_player = {"NAME": "Jordan", "HELD_DICE": []}

        pluck_dice(test_player, test_roll, test_desired_dice)
        result = test_player["HELD_DICE"]
        expected = [1, 1, 3, 3, 4]

        self.assertEqual(result, expected)
