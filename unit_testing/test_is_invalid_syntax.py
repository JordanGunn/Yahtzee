import unittest
from yahtzee import is_invalid_syntax


class TestIsInvalidSyntax(unittest.TestCase):

    def test_is_invalid_syntax_not_a_command(self):

        test_command = ['fake', 'fake fake']

        result = is_invalid_syntax(test_command)
        expected = True

        self.assertEqual(result, expected)

    def test_is_invalid_syntax_missing_args(self):

        test_command = ['pluck']

        result = is_invalid_syntax(test_command)
        expected = True

        self.assertEqual(result, expected)

    def test_is_invalid_syntax_syntax_is_valid(self):

        test_command = ['pluck', '1 1 1']

        result = is_invalid_syntax(test_command)
        expected = False

        self.assertEqual(result, expected)