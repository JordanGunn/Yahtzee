from typing import Union


def VALID_INPUT():

    """
    Return constant VALID_INPUT

    Copied an adapted from Assignment 2: books.py
    """


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

    pass


def SCORECARD() -> dict:

    """
    Return scorecard template.

    Returns a an empty scorecard template to be used at
    the beginning of a new game.

    :return: scorecard
    """

    pass


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
    :precondition:       The argument <number_dice> must be
                         between 1 and 5 (inclusive).
    :postcondition:      Will return a list of length <number_dice>
                         containing random numbers between 1 and 6.
    :return:             List of rolled di.
    """

    pass


def create_player(name: str) -> dict:

    """
    Create a player for the game.

    Create a player with attributes: dice_held scorecard, and name.

    :param name:        Name of the player.
    :precondition:      The argument <name> must be a string.
    :postcondition:     Will create a player to use in yahtzee()
                        containing attributes necessary for gameplay.
    :return:            Player with attributes.
    """

    pass


def check_multiple_die(roll: list, repetition: int) -> int:

    """
    Check for multiple of the same di in a roll.

    Copied and adapted from lab06: Regex
    Intended to be used to search for repetition of 3 or greater and
    returns points. If <repetition> number == 5, and a match is
    successful (ie yahtzee), function will always return 50.

    :param roll:         A list of random numbers
    :param repetition:   The repeated value to search for.
    :precondition:       <roll> must be a list if ints between 1 and 6.
    :postcondition:      Will perform pattern recognition
                         to detect multiple recurring die
                         in a roll.
    :return:             Regex match (list).

    >>> check_multiple_die([3, 3, 3, 2, 1], 3)
    12
    >>> check_multiple_die([1, 2, 3, 4, 5], 3)
    0
    >>> check_multiple_die([5, 5, 5, 5, 5], 5)
    50
    """

    pass


def check_small_straight(roll: list) -> int:

    """
    Check for straight.

    Copied and adapted from lab06: Regex.
    Checks for small straight and returns points.

    :param roll:    A list of random numbers.
    :precondition:  <roll> must be a list ints between 1 and 6.
    :postcondition: Will perform pattern recognition to detect a straight.
    :return:        Regex match (list).
    >>> check_small_straight([1, 2, 3, 4, 6])
    30
    >>> check_small_straight([1, 2, 3, 4, 5])
    30
    >>> check_small_straight([1, 3, 5, 6, 3])
    0
    """

    pass


def check_large_straight(roll: list) -> int:

    """
    Check for straight.

    Copied and adapted from lab06: Regex.
    Checks for large straight and returns points.

    :param roll:    A list of random numbers.
    :precondition:  <roll> must be a list of ints between 1 and 6.
    :postcondition: Will perform pattern recognition to detect a straight.
    :return:        Regex match (list).
    >>> check_large_straight([1, 2, 3, 4, 6])
    0
    >>> check_large_straight([1, 2, 3, 4, 5])
    40
    >>> check_large_straight([1, 3, 5, 6, 3])
    0
    """

    pass


def check_number(roll: list, value: int) -> int:

    """
    Check for collection of number.

    Copied and adapted from Lab06: Regex.
    Checks for one or more of a specific number
    and returns points.

    :param roll:    A list of random numbers.
    :param value:   The value to search for.
    :precondition:  The argument <roll> must be a list of
                    number between 1 and 6.
    :postcondition: Will perform pattern recognition
                    to detect any instance of a particular
                    number in <roll>.
    :return:        Regex match (list).

    >>> check_number([5, 5, 5, 2, 2], 5)
    15
    >>> check_number([5, 2, 2, 2, 2], 5)
    5
    >>> check_number([2, 2, 2, 2, 2], 5)
    0
    >>> check_number([2, 2, 2, 2, 2], 2)
    10
    """

    pass


def check_full_house(roll: list) -> int:

    """
    Check for a full-house and returns points.

    Copied and adapted from Lab06: Regex.

    :param roll:    A list of random numbers.
    :precondition:  <roll> must be a list of sorted ints
                    between 1 and 6.
    :postcondition: Will perform pattern recognition
                    to detect a full house in a roll.
    :return:        Regex match (list).

    >>> check_full_house([2, 2, 2, 3, 3])
    25
    >>> check_full_house([2, 2, 3, 3, 3])
    25
    >>> check_full_house([2, 2, 2, 2, 3])
    0
    """

    pass


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

    pass


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
    :postcondition:         Will place <desired_dice> in a player's
                            attribute "held_dice".
    :return:                A subset of numbers from <roll>.
    """

    pass


def remove_dice(player: dict, roll: list, dice_selection: str):

    """
    Pull dice from held dice.

    :param player:          A yahtzee player (dict).
    :param roll:            A list of random numbers
    :param dice_selection:  Dice you wish to remove from player's
                            held dice.
    :precondition:          The argument <dice_selection> must be a
                            space delimited string of numbers between
                            1 and 6 inclusive.
    :postcondition:         Will place <desired_dice> in a player's
                            attribute "held_dice".
    :return:                A subset of numbers from <roll>.
    """

    pass


def is_next_turn(command: list) -> bool:

    """
    Determine if player's next turn should begin.

    Controls whether or not to increase the
    turn count in yahtzee.

    :param command: A list with command and args.
    :precondition:  Command is a list.
    :postcondition: Will determine return true or false.
    :return:        True or False (bool).

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

    :param command: A list with command and args.
    :return:        True or False (bool)

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


def add_score(player: dict, field: str, score: Union[int, str]):

    """
    Add score to player scorecard.

    Player can also "scratch" a score if no options are available.

    :param player:  A yahtzee player (dict).
    :param score:   Score to submit to scorecard.
    :param field:   Score field you wish to update.
    :precondition:  Argument <field> must be a valid scorecard key.
    :postcondition: Will update the player's current score.
    """

    pass


def is_bonus(player: dict) -> bool:

    """
    Determine is player is awarded bonus.

    Check if upper section of player's scorecard
    is greater than or equal to 63.

    :param player: A yahtzee player (dict).
    :return: True or False.

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
    :return:        True or False.

    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 63}})
    True
    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 33, "twos": 0}})
    False
    """

    pass


def get_final_score(player: dict) -> dict:

    """
    Calculate player's final score.

    :param player:  A yahtzee player (dict).
    :precondition:  Argument <player> must pass boolean
                    function is_player_done().
    :postcondition: Will return players lower score, upper score
                    final score, and name.
    :return:        Final score (name & score).

    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 63}})
    {"NAME": Jordan, "final_score": 63}
    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 33, "twos": 0}})
    {"NAME": Jordan, "final_score": 33}
    >>> is_bonus({"NAME": "Jordan", "SCORECARD": {"ones": 1, "twos": 2}})
    {"NAME": Jordan, "final_score": 3}
    """

    pass

