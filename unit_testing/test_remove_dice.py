import unittest
from yahtzee import remove_dice


class TestPluckDice(unittest.TestCase):

    def test_remove_dice_remove_all(self):

        test_roll = [1, 2]
        test_dice_selection = "1 1 3"
        test_player = {"NAME": "Jordan", "HELD_DICE": [1, 1, 3]}

        remove_dice(test_player, test_roll, test_dice_selection)
        result = test_player["HELD_DICE"]
        expected = []

        self.assertEqual(result, expected)

    def test_remove_dice_remove_one_with_multiple(self):

        test_roll = [3, 4]
        test_dice_selection = "2"
        test_player = {"NAME": "Jordan", "HELD_DICE": [2, 2, 3]}

        remove_dice(test_player, test_roll, test_dice_selection)
        result = test_player["HELD_DICE"]
        expected = [2, 3]

        self.assertEqual(result, expected)

    def test_remove_dice_added_back_to_roll(self):

        test_roll = [1, 2]
        test_dice_selection = "2"
        test_player = {"NAME": "Jordan", "HELD_DICE": [2, 2, 3]}

        remove_dice(test_player, test_roll, test_dice_selection)
        result = test_roll
        expected = [1, 2, 2]

        self.assertEqual(result, expected)
