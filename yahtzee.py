def HELP():

    """
    Print help menu.
    """

    pass


def DI() -> list:

    """
    Return constant DI.

    Returns a list of all values for a six-sided di.

    :return: List of values.
    """

    pass


def RENDER_DI() -> dict:

    """
    Return constant di.

    Returns a dictionary of ASCII represented
    di faces (1~6).

    :return: All faces of 6 sided di.
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


def roll_dice(number_dice_: int) -> list:

    """
    Roll a set of dice.

    Roll a set of six sided di and return a list of the
    rolled numbers.

    :param number_dice_: Number of dice you wish to roll.
    :return:             List of rolled di.
    """

    pass


def create_player(name: str, scorecard: dict) -> dict:

    """
    Create a player for the game.

    Create a player with attributes: dice_held, roll_number
    scorecard, and name.

    :param name:        Name of the player.
    :param scorecard:   An empty scorecard.
    :return:            Player with attributes.
    """

    pass


def check_multiple_di(roll: list, value: int) -> list:

    """
    Check for multiple of the same di in a roll.

    :param roll:    A list of random numbers
    :param value:   The repeated value to search for.
    :return:        Regex match (list).
    """

    pass


def check_straight(roll: list) -> list:

    """
    Check for straight.

    Checks for small or large straight.

    :param roll: A list of random numbers.
    :return:     Regex match (list).
    """

    pass


def check_number(roll: list, value: int) -> list:

    """
    Check for collection of number.

    Checks for one or more of a specific number.

    :param roll:    A list of random numbers.
    :param value:   The value to search for.
    :return:        Regex match (list).
    """

    pass


def check_full_house(roll: list) -> list:

    """
    Check for a full-house.

    :param roll: A list of random numbers.
    :return:     Regex match (list).
    """

    pass


def get_available_scores(roll: list, player: dict, scratch=False) -> dict:

    """
    Determine available scores from players held dice.

    :param roll:    A list of random numbers.
    :param player:  A yahtzee player (dict).
    :param scratch: Boolean which will display available
                    scratch values if set to True.
    :return:        Available scores.
    """

    pass


def turn(player: dict):

    """
    Execute a turn of yahtzee.

    :param player: A yahtzee player (dict).
    """

    pass


def choose_dice(roll: list) -> list:

    """
    Pull dice from roll and pass to player.

    :param roll:  A list of random numbers.
    :return:      A subset of random numbers.
    """

    pass


def show_score(player: dict) -> list:

    """
    Show players current SCORECARD.

    :param player: A yahtzee player (dict).
    """

    pass


def add_score(player: dict, field: str, score: int):

    """
    Add score to player scorecard.

    :param score: Score to submit to scorecard.
    :param field: Score field you wish to update.
    :param player: A yahtzee player (dict).
    """

    pass


def is_bonus(player: dict) -> bool:

    """
    Determine is player is awarded bonus.

    :param player: A yahtzee player (dict).
    :return: True or False.
    """

    pass


def is_player_done(player: dict) -> bool:

    """
    Determine if player is finished yahtzee.

    :param player:  A yahtzee player (dict).
    :return:        True or False.
    """

    pass


def get_final_score(player: dict) -> dict:

    """
    Calculate player's final score.

    :param player:  A yahtzee player (dict).
    :return:        Final score (name & score).
    """

    pass

