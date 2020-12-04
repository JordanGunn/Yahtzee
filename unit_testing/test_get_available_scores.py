import unittest
from ..yahtzee import get_available_scores


class TestGetAvailableScores(unittest.TestCase):

    def test_get_available_scores_from_empty_held_dice(self):

        test_roll = [1, 1, 3, 4, 3]

        player = {
            'name': 'Jordan', 'dice_held': [],
            'scorecard': {
                'ones': 0,
                'twos': 0,
                'threes': 0,
                'fours': 0,
                'chance': 0
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {'ones': 2, 'threes': 6, 'fours': 4, 'chance': 12}

        self.assertEqual(result, expected)

    def test_get_available_scores_from_held_dice(self):

        test_roll = []

        player = {
            'name': 'Jordan', 'dice_held': [1, 1, 3, 4, 3],
            'scorecard': {
                'ones': 0,
                'twos': 0,
                'threes': 0,
                'fours': 0
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {'ones': 2, 'threes': 6, 'fours': 4}

        self.assertEqual(result, expected)

    def test_get_available_scores_no_available_scores(self):

        test_roll = []

        player = {
            'name': 'Jordan', 'dice_held': [1, 1, 3, 4, 3],
            'scorecard': {
                'ones': 3,
                'twos': 6,
                'threes': 9,
                'fours': 12
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {}

        self.assertEqual(result, expected)

    def test_get_available_scores_from_roll_and_held_dice(self):

        test_roll = [1, 1, 3]

        player = {
            'name': 'Jordan', 'dice_held': [4, 3],
            'scorecard': {
                'ones': 0,
                'twos': 0,
                'threes': 0,
                'fours': 0
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {'ones': 2, 'threes': 6, 'fours': 4}

        self.assertEqual(result, expected)

    def test_get_available_scores_yahtzee(self):

        test_roll = [3, 3]

        player = {
            'name': 'Jordan', 'dice_held': [3, 3, 3],
            'scorecard': {
                'threes': 0,
                'full_house': 0,
                'three_of_a_kind': 0,
                'four_of_a_kind': 0,
                'yahtzee': 0
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {'threes': 15, 'three_of_a_kind': 15, 'four_of_a_kind': 15, 'yahtzee': 50}

        self.assertEqual(result, expected)

    def test_get_available_scores_fields_filled(self):

        test_roll = [4, 4]

        player = {
            'name': 'Jordan', 'dice_held': [4, 4, 3],
            'scorecard': {
                'fours': 16,
                'full_house': 0,
                'three_of_a_kind': 0,
                'four_of_a_kind': 0,
                'yahtzee': 0
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {'three_of_a_kind': 19, 'four_of_a_kind': 19}

        self.assertEqual(result, expected)

    def test_get_available_scores_fields_filled(self):

        test_roll = [5, 5]

        player = {
            'name': 'Jordan', 'dice_held': [5, 5, 3],
            'scorecard': {
                'fives': 20,
                'full_house': 0,
                'three_of_a_kind': 0,
                'four_of_a_kind': 0,
                'yahtzee': 0
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {'three_of_a_kind': 19, 'four_of_a_kind': 19}

        self.assertEqual(result, expected)