from typing import Union
import random
import re


def VALID_INPUT():

    """
    Return constant VALID_INPUT.

    Copied an adapted from Assignment 2: books.py
    """

    return ['pluck', 'remove', 'submit', 'scratch', 'help', 'quit']


def HELP():

    """
    Print help menu.

    Copied and adapted from Assignment 2: books.py
    """

    pass


def DIE() -> list:

    """
    Return constant DIE.

    Returns a list of all values for a six-sided die.

    :return: List of values.
    """

    return [1, 2, 3, 4, 5, 6]


def FIXED_SCORES() -> dict:

    """
    Return constant FIXED_SCORES.

    A dictionary of fixed score values.

    :return: FIXED_SCORES
    """

    fixed_scores = {"FULL_HOUSE": 25, "SMALL_STRAIGHT": 30, "LARGE_STRAIGHT": 40, "YAHTZEE": 50}

    return fixed_scores


def SCORECARD() -> dict:

    """
    Return scorecard template.

    Returns a an empty scorecard template to be used at
    the beginning of a new game.

    :return: SCORECARD
    """

    scorecard = {
        "ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0,
        "three of a kind": 0, "four of a kind": 0, "full house": 0,
        "small_straight": 0, "large straight": 0,
        "yahtzee": 0, "chance": 0
    }

    return scorecard


def yahtzee():

    """
    Run the yahtzee game.

    Front-end function.
    """

    pass


def roll_dice(number_dice: int) -> list:

    """
    Roll a set of dice.

    Roll a set of six sided di and return a list of the
    rolled numbers.

    :param number_dice:  Number of dice you wish to roll.
    :precondition:       <number_dice> must be int between 1 and 5 (inclusive).
    :postcondition:      Will return a list of length <number_dice>
                         containing random numbers between 1 and 6.
    :return:             List of rolled di.
    """

    roll = sorted([random.randint(min(DIE()), max(DIE())) for _ in range(number_dice)])

    return roll


def roll_to_string(roll: list) -> str:

    """
    Convert dice roll to string.

    Convert roll to string for regex searching.

    :param roll:    a list of ints between 1 and 6 inclusive.
    :precondition:  <roll> must be generated from roll_dice().
    :postcondition: Will generate a joined string of ints in roll.
    :return:        roll as a string

    """

    casted_die = [str(die) for die in roll]

    return "".join(casted_die)


def create_player(name: str) -> dict:

    """
    Create a player for the game.

    Create a player with attributes: HELD_DICE, SCORECARD, and NAME.

    :param name:        Name of the player.
    :precondition:      The argument <name> must be a string.
    :postcondition:     Will create a player to use in yahtzee()
                        containing attributes necessary for gameplay.
    :return:            Player with attributes.
    """

    player = {
        "NAME": name, "HELD_DICE": [], "SCORECARD": SCORECARD()
    }

    return player


def check_multiple_die(roll: list, repetition: int) -> int:

    """
    Check for multiple repeating die in a roll.

    Copied and adapted from lab06: Regex
    Intended to be used to search for repetition of 3 or greater and
    return points. If <repetition> == 5, and a match is successful,
    function will always return FIXED_SCORES()["YAHTZEE"].

    :param roll:         A list of random numbers
    :param repetition:   The repeated value to search for.
    :precondition:       <roll> must be a list of sorted ints between 1 and 6.
    :postcondition:      Perform pattern recognition to detect multiple repeating die
    :return:             Points.

    >>> check_multiple_die([3, 3, 3, 2, 1], 3)
    12
    >>> check_multiple_die([1, 2, 3, 4, 5], 3)
    0
    >>> check_multiple_die([5, 5, 5, 5, 5], 5)
    50
    """

    # convert roll list to string for regex
    dice = roll_to_string(roll)

    # build regex argument as string
    repeating_regex_str = r'([1-6])(\1{' + str(repetition-1) + r'})'

    # compile regex object and search
    repeating = re.compile(repeating_regex_str)
    repeating_find = repeating.findall(dice)

    # if repetition equals 5, YAHTZEE
    if repeating_find and repetition == 5:
        return FIXED_SCORES()["YAHTZEE"]

    # four or three of a kind
    if repeating_find:
        return sum(roll)

    # return 0 if no conditions met
    return 0


def check_small_straight(roll: list) -> int:

    """
    Check for straight.

    Copied and adapted from lab06: Regex.
    Checks for small straight and returns points.

    :param roll:    A list of random numbers.
    :precondition:  <roll> must be a list of sorted ints between 1 and 6.
    :postcondition: Perform pattern recognition to for a small straight.
    :return:        Points.
    >>> check_small_straight([1, 2, 3, 4, 6])
    30
    >>> check_small_straight([1, 2, 3, 4, 5])
    30
    >>> check_small_straight([1, 3, 5, 6, 3])
    0
    """

    # get min, max from roll
    dice_min, dice_max = str(min(roll)), str(max(roll))

    # remove internal repetition, cast to string
    dice = roll_to_string(sorted(list(set(roll))))

    # convert die constant to a string for regex
    die_string = [str(die) for die in DIE()]

    # compile regex object and search
    straight_check = re.compile(dice)
    # search roll with internal repetition
    if straight_check.search("".join(die_string)) and len(dice) == 4:
        return FIXED_SCORES()["SMALL_STRAIGHT"]

    # search roll with 5 dice non repeating
    if len(dice) > 4:

        # remove max and min to check for "hanging" numbers
        min_straight_check = re.compile(dice.replace(dice_min, ""))
        max_straight_check = re.compile(dice.replace(dice_max, ""))

        # search
        min_find = min_straight_check.search("".join(die_string))
        max_find = max_straight_check.search("".join(die_string))

        # get the points
        if min_find or max_find:
            return FIXED_SCORES()["SMALL_STRAIGHT"]

    # return 0 if no conditions met
    return 0


def check_large_straight(roll: list) -> int:

    """
    Check for straight.

    Copied and adapted from lab06: Regex.
    Checks for large straight and returns points.

    :param roll:    A list of random numbers.
    :precondition:  <roll> must be a list of sroted ints between 1 and 6.
    :postcondition: Will perform pattern recognition for a large straight.
    :return:        Points.

    >>> check_large_straight([1, 2, 3, 4, 6])
    0
    >>> check_large_straight([1, 2, 3, 4, 5])
    40
    >>> check_large_straight([1, 3, 5, 6, 3])
    0
    """

    # cast to string and sort for good measure
    dice = roll_to_string(sorted(roll))

    # convert di constant to a string
    die_string = [str(die) for die in DIE()]

    # compile regex object
    straight_check = re.compile(dice)

    # search and return
    if straight_check.search("".join(die_string)):
        return FIXED_SCORES()["LARGE_STRAIGHT"]

    # return 0 if no conditions met
    return 0


def check_number(roll: list, value: int) -> int:

    """
    Check for collection of number.

    Copied and adapted from Lab06: Regex.
    Checks for one or more of a specific number.

    :param roll:    A list of random numbers.
    :param value:   The value to search for.
    :precondition:  <roll> must be a list of sorted ints between 1 and 6.
    :postcondition: Perform pattern recognition for any instance of <value>
    :return:        Points.

    >>> check_number([5, 5, 5, 2, 2], 5)
    15
    >>> check_number([5, 2, 2, 2, 2], 5)
    5
    >>> check_number([2, 2, 2, 2, 2], 5)
    0
    >>> check_number([2, 2, 2, 2, 2], 2)
    10
    """

    # cast to string and sort for good measure
    dice = roll_to_string(sorted(roll))

    # create regex string and compile
    number_regex_string = f'{value}' + '{,5}'
    number_regex = re.compile(number_regex_string)

    # look for match
    number_find = number_regex.findall(dice)

    if number_find:
        # convert numbers back to ints
        number_find_ints = [int(number) for number in "".join(number_find)]
        # get the sum
        return sum(number_find_ints)

    # return 0 if no conditions met
    return 0


def check_full_house(roll: list) -> int:

    """
    Check for a full-house and returns points.

    Copied and adapted from Lab06: Regex.

    :param roll:    A list of random numbers.
    :precondition:  <roll> must be a list of sorted ints between 1 and 6.
    :postcondition: Perform pattern recognition to detect a full house.
    :return:        Points.

    >>> check_full_house([2, 2, 2, 3, 3])
    25
    >>> check_full_house([2, 2, 3, 3, 3])
    25
    >>> check_full_house([2, 2, 2, 2, 3])
    0
    """

    # cast to string and sort for good measure
    dice = roll_to_string(sorted(roll))

    # build three of a kind regex and search
    three_kind_regex = re.compile(r'([1-6])(\1{2})')
    three_kind_find = three_kind_regex.findall(dice)
    three_string = ["".join(find) for find in three_kind_find]

    # build pair regex
    pair_regex = re.compile(r'([1-6])(\1)')

    # check for 3 of a kind
    if three_kind_regex.findall(dice):
        # if three of a kind, and look for pair
        pair = dice.replace(three_string[0], "")
        if pair_regex.findall(pair) and not check_multiple_die(roll, 5):
            return FIXED_SCORES()["FULL_HOUSE"]
    return 0


def get_available_scores(roll: list, player: dict, scratch=False) -> dict:

    """
    Determine available scores from players held dice.

    Determines and returns the available scores based on
    a player's held dice and the current roll dice. If
    scratch=True, function will return empty score fields.

    :param roll:    A list of random numbers.
    :param player:  A yahtzee player (dict).
    :param scratch: Boolean which will display available
                    scratch values if set to True.
    :precondition:  Player must be active.
    :postcondition: Will perform pattern recognition
                    to detect a full house in a roll.
    :return:        Available scores.

    >>> get_available_scores([5, 5, 5, 5, 5], {"NAME": "Jordan", "HELD_DICE": [], "SCORECARD": {"yahtzee": 0}})
    {"yahtzee": 50}
    >>> get_available_scores([5, 5, 5], {"NAME": "Jordan", "HELD_DICE": [5, 5], "SCORECARD": {"yahtzee": 0}})
    {"yahtzee": 50}
    >>> get_available_scores([], {"NAME": "Jordan", "HELD_DICE": [5, 5, 5, 5, 5], "SCORECARD": {"yahtzee": 0}})
    {"yahtzee": 50}
    """

    # combine held_dice and rolled dice
    dice = sorted(player["HELD_DICE"] + roll)

    # calculate top scoresheet (1s through 6s)
    scoresheet_top = [check_number(dice, number) for number in range(1, 7)]

    # calculate bottom scoresheet
    scoresheet_bottom = [
        check_multiple_die(dice, 3), check_multiple_die(dice, 4), check_full_house(dice),
        check_small_straight(dice), check_large_straight(dice), check_multiple_die(dice, 5),
        sum(dice)
    ]

    calculated_scores = scoresheet_top + scoresheet_bottom

    calc_and_keys = zip(calculated_scores, player["SCORECARD"].keys())

    if scratch:
        available_scores = {key: "scratch" for key in player["SCORECARD"] if player["SCORECARD"][key] == 0}

    # else:
        # available_scores = {key:value for value, key in calc_and_keys if }


def is_valid_score(player, key, score):

    """
    Determine if score is valid to display.

    :param player: A yahtzee player object.
    :param key: A key in a player's scorecard.
    :param score: A score value
    :return: True or False (bool).
    """

    valid_score = (
        (player["SCORECARD"][key] != "scratch" and score != 0) and
        player["SCORECARD"][key] == 0
    )

    return valid_score


def turn(player: dict):

    """
    Execute a turn of yahtzee.

    Helper function for yahtzee().
    Simulates a player's "turn" in yahtzee.

    :param player: A yahtzee player (dict).
    """

    pass


def run_command(command: list, player: dict):

    """
    Execute command from yahtzee prompt.

    Copied and adapted from Assigment 2: books.py

    :param command:
    :param player:
    :return:
    """

    pass


def format_user_input(command_string: str) -> list:

    """
    Parse user input from yahtzee prompt.

    Copied and adapted from Assignment 2: books.py

    :param command_string: a string from yahtzee prompt
    :precondition:         Input must be a string
    :postcondition:        Will format string as a yahtzee command.
    :return:               A command and a list of args.

    >>> format_user_input("pluck 2 2")
    ["pluck", "2 2 2"]
    >>> format_user_input("")
    [""]
    >>> format_user_input("submit ones")
    ["submit", "ones"]
    """


def pluck_dice(player: dict, roll: list, desired_dice: str):

    """
    Pull dice from roll and pass to player.

    :param player:          A yahtzee player (dict).
    :param roll:            A list of random numbers.
    :param desired_dice:    Dice you wish to pluck from <roll>
    :precondition:          <roll> must be a list of ints between 1 and 6.
    :postcondition:         Place <desired_dice> in a player's "HELD_DICE".
    """

    # convert list of ints to list of chars
    dice = list(roll_to_string(roll))
    # create list of chars from desired dice
    desired_dice_list = sorted(desired_dice.split(" "))

    # pluck dice from roll, convert back to int
    plucked = [
        int(dice.pop(dice.index(die))) for die in desired_dice_list if die in dice
    ]

    [roll.remove(pluck) for pluck in plucked]

    player["HELD_DICE"] += plucked


def remove_dice(player: dict, roll: list, desired_dice: str):

    """
    Pull dice from held dice.

    :param player:          A yahtzee player (dict).
    :param roll:            A list of random ints
    :param desired_dice:    Dice you wish to remove from player's held dice.
    :precondition:          <desired_dice> must be a space delimited string of
                            numbers between 1 and 6 inclusive.
    :postcondition:         Will place <desired_dice> back into <roll>
    """

    # cast elements to integers
    desired_dice_int = sorted([int(die) for die in desired_dice.split(" ")])

    # remove from player's held dice
    [player["HELD_DICE"].remove(die) for die in desired_dice_int if die in player["HELD_DICE"]]

    # add back to roll
    [roll.append(die) for die in desired_dice_int]


def is_next_turn(command: list) -> bool:

    """
    Determine if player's next turn should begin.

    Controls whether or not to increase the
    turn count in yahtzee.

    :param command:     A list with command and args.
    :precondition:      Command is a list.
    :postcondition:     Will determine if player should roll again.
    :return:            True or False (bool).

    >>> is_next_turn([""])
    True
    >>> is_next_turn(["fake"])
    False
    >>> is_next_turn(["pluck", "2 2"])
    False
    """


def is_turn_over(command: list) -> bool:

    """
    Determine if player's turn ends.

    Used to end a player's turn prematurely.

    :param command:     A list with command and args.
    :precondition:      <command> must be ouput of format_user_input()
    :postcondition:     Will decide whether to end player's turn.
    :return:            True or False (bool)

    >>> is_turn_over(["submit", "ones"])
    True
    >>> is_turn_over(["scratch", "ones"])
    True
    >>> is_turn_over(["fake"])
    False
    """


def is_valid_syntax(command: list) -> bool:

    """
    Determine is command at yahtzee prompt is valid.

    :param command: A list with command and args.
    :precondition:  <command> must be output from format_user_input().
    :postcondition: Will check for invalid commands or syntax.
    :return:        True or False (bool)

    >>> is_valid_syntax(["pluck", "2", "2"])
    False
    >>> is_valid_syntax(["pluck", "2 2"])
    True
    >>> is_valid_syntax(["pluck"])
    False
    >>> is_valid_syntax(["fake"])
    False
    """


def submit_score(player: dict, field: str, score: Union[int, str]):

    """
    Add score to player scorecard.

    Player can also "scratch" a score if no options are available.

    :param player:  A yahtzee player (dict).
    :param score:   Score to submit to scorecard.
    :param field:   Score field you wish to update.
    :precondition:  <field> must be a valid scorecard key.
    :postcondition: Update the player's current score.
    """

    pass


def is_bonus(player: dict) -> bool:

    """
    Determine is player is awarded bonus.

    Check if upper section of player's scorecard
    is greater than or equal to 63.

    :param player:  A yahtzee player (dict).
    :precondition:  Player must be a yahtzee player object.
    :postcondition: Will decide whether player should receive score bonus.
    :return:        True or False (bool).

    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 63}})
    True
    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 62}})
    False
    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 33, "twos": 33}})
    True
    """

    pass


def is_player_done(player: dict) -> bool:

    """
    Determine if player is finished yahtzee.

    Check all scorecard fields to determine if player
    has completed the game.

    :param player:  A yahtzee player (dict).
    :precondition:  <player> must be a yahtzee player object.
    :postcondition: Will decide whether to pull a player from the game.
    :return:        True or False.

    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 63}})
    True
    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 33, "twos": 0}})
    False
    """

    pass


def get_final_score(player: dict) -> dict:

    """
    Calculate player's total score.

    :param player:  A yahtzee player (dict).
    :precondition:  <player> must be a yahtzee player object.
    :postcondition: Will return players total score.
    :return:        Final score (name & score).

    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 63}})
    {"NAME": Jordan, "final_score": 63}
    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 33, "twos": 0}})
    {"NAME": Jordan, "final_score": 33}
    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 1, "twos": 2}})
    {"NAME": Jordan, "final_score": 3}
    """

    pass

