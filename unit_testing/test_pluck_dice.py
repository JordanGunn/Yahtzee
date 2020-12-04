import unittest
from ..yahtzee import pluck_dice


class TestPluckDice(unittest.TestCase):

    def test_pluck_dice_empty_held_dice(self):

        test_roll = [1, 1, 3, 4, 3]
        test_desired_dice = "1 1 3"
        test_player = {"name": "Jordan", "dice_held": []}

        pluck_dice(test_player, test_roll, test_desired_dice)
        result = test_player["dice_held"]
        expected = [1, 1, 3]

        self.assertEqual(result, expected)

    def test_pluck_dice_add_to_held_dice(self):

        test_roll = [4, 3]
        test_desired_dice = "4"
        test_player = {"name": "Jordan", "dice_held": [1, 1, 3]}

        pluck_dice(test_player, test_roll, test_desired_dice)
        result = test_player["dice_held"]
        expected = [1, 1, 3, 4]

        self.assertEqual(result, expected)

    def test_pluck_dice_remove_all_dice(self):

        test_roll = [4, 3, 1, 1, 3]
        test_desired_dice = "4 3 1 1 3"
        test_player = {"name": "Jordan", "dice_held": []}

        pluck_dice(test_player, test_roll, test_desired_dice)
        result = test_player["dice_held"]
        expected = [4, 3, 1, 1, 3]

        self.assertEqual(result, expected)
