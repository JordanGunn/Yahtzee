import unittest
from yahtzee import get_available_scores


class TestGetAvailableScores(unittest.TestCase):

    def test_get_available_scores_from_empty_held_dice(self):

        test_roll = [1, 1, 3, 3, 4]

        player = {
            'NAME': 'Jordan', 'HELD_DICE': [],
            'SCORECARD': {
                "ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0,
                "three of a kind": 0, "four of a kind": 0, "full house": 0,
                "small straight": 0, "large straight": 0,
                "yahtzee": 0, "chance": 0
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {'ones': 2, 'threes': 6, 'fours': 4, 'chance': 12}

        self.assertEqual(result, expected)

    def test_get_available_scores_from_held_dice(self):

        test_roll = []

        player = {
            'NAME': 'Jordan', 'HELD_DICE': [1, 1, 3, 3, 4],
            'SCORECARD': {
                "ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0,
                "three of a kind": 0, "four of a kind": 0, "full house": 0,
                "small straight": 0, "large straight": 0,
                "yahtzee": 0, "chance": 0
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {'ones': 2, 'threes': 6, 'fours': 4, 'chance': 12}

        self.assertEqual(result, expected)

    def test_get_available_scores_no_available_scores(self):

        test_roll = []

        player = {
            'NAME': 'Jordan', 'HELD_DICE': [1, 1, 3, 3, 4],
            'SCORECARD': {
                "ones": 3, "twos": 6, "threes": 9, "fours": 12, "fives": 0, "sixes": 0,
                "three of a kind": 0, "four of a kind": 0, "full house": 0,
                "small straight": 0, "large straight": 0,
                "yahtzee": 0, "chance": 12
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {}

        self.assertEqual(result, expected)

    def test_get_available_scores_from_roll_and_held_dice(self):

        test_roll = [1, 1, 3]

        player = {
            'NAME': 'Jordan', 'HELD_DICE': [3, 4],
            'SCORECARD': {
                "ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0,
                "three of a kind": 0, "four of a kind": 0, "full house": 0,
                "small straight": 0, "large straight": 0,
                "yahtzee": 0, "chance": 12
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {'ones': 2, 'threes': 6, 'fours': 4}

        self.assertEqual(result, expected)

    def test_get_available_scores_yahtzee(self):

        test_roll = [3, 3]

        player = {
            'NAME': 'Jordan', 'HELD_DICE': [3, 3, 3],
            'SCORECARD': {
                "ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0,
                "three of a kind": 0, "four of a kind": 0, "full house": 0,
                "small straight": 0, "large straight": 0,
                "yahtzee": 0, "chance": 15
            }
        }

        result = get_available_scores(test_roll, player)
        expected = {'threes': 15, 'three of a kind': 15, 'four of a kind': 15, 'yahtzee': 50}

        self.assertEqual(result, expected)

    def test_get_available_scores_for_scratch(self):

        test_roll = [4, 4]

        player = {
            'NAME': 'Jordan', 'HELD_DICE': [3, 3, 4],
            'SCORECARD': {
                "ones": 0, "twos": 0, "threes": 0, "fours": 16, "fives": 0, "sixes": 0,
                "three of a kind": 0, "four of a kind": 0, "full house": 0,
                "small straight": 0, "large straight": 0,
                "yahtzee": 0, "chance": 11
            }
        }

        result = get_available_scores(test_roll, player, scratch=True)
        expected = {
            "ones": "scratch", "twos": "scratch", "threes": "scratch", "fives": "scratch",
            "sixes": "scratch", "full house": "scratch", "three of a kind": "scratch",
            "four of a kind": "scratch", "small straight": "scratch",
            "large straight": "scratch", "yahtzee": "scratch"
        }

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
