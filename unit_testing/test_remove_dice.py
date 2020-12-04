import unittest
from ..yahtzee import remove_dice


class TestPluckDice(unittest.TestCase):

    def test_remove_dice_remove_all(self):

        test_dice_selection = "1 1 3"
        test_player = {"name": "Jordan", "dice_held": [1, 1, 3]}

        remove_dice(test_player, test_dice_selection)
        result = test_player["dice_held"]
        expected = []

        self.assertEqual(result, expected)

    def test_remove_dice_remove_one_with_multiple(self):

        test_dice_selection = "2"
        test_player = {"name": "Jordan", "dice_held": [2, 2, 3]}

        remove_dice(test_player, test_dice_selection)
        result = test_player["dice_held"]
        expected = [2, 3]

        self.assertEqual(result, expected)
