import unittest
from yahtzee import is_turn_over


class TestIsTurnOver(unittest.TestCase):

    def test_is_turn_over_submit(self):

        test_command = ['submit', 'ones']

        result = is_turn_over(test_command)
        expected = True

        self.assertEqual(result, expected)

    def test_is_turn_over_scratch(self):

        test_command = ['scratch', 'ones']

        result = is_turn_over(test_command)
        expected = True

        self.assertEqual(result, expected)

    def test_is_turn_over_turn_not_over(self):

        test_command = ['pluck', '1 1 1']

        result = is_turn_over(test_command)
        expected = False

        self.assertEqual(result, expected)

    def test_is_turn_over_missing_args(self):

        test_command = ['submit']

        result = is_turn_over(test_command)
        expected = False

        self.assertEqual(result, expected)