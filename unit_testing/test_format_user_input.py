import unittest
from yahtzee import format_user_input


class TestFormatUserInput(unittest.TestCase):

    def test_format_user_input_one_string_value(self):

        test_command_string = 'pluck 2'

        expected = ['pluck', '2']
        result = format_user_input(test_command_string)
        self.assertEqual(result, expected)

    def test_format_user_input_multi_string_value(self):

        test_command_string = 'pluck 2 2 2'

        expected = ['pluck', '2 2 2']
        result = format_user_input(test_command_string)
        self.assertEqual(result, expected)
