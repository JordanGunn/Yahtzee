import unittest
from unittest.mock import patch
from yahtzee import roll_dice


class TestRollDice(unittest.TestCase):

    @patch("random.randint")
    def test_roll_dice_min_di(self, mock_randint):

        mock_randint.return_value = 6

        result = roll_dice(1)
        expected = [6]

        self.assertEqual(result, expected)

    @patch("random.randint")
    def test_roll_dice_max_di(self, mock_randint):
        mock_randint.return_value = 6

        result = roll_dice(5)
        expected = [6, 6, 6, 6, 6]

        self.assertEqual(result, expected)

    @patch("random.randint")
    def test_roll_dice_three_di(self, mock_randint):
        mock_randint.return_value = 6

        result = roll_dice(3)
        expected = [6, 6, 6]

        self.assertEqual(result, expected)

