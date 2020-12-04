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


def roll_dice(number_dice: int) -> list:

    """
    Roll a set of dice.

    Roll a set of six sided di and return a list of the
    rolled numbers.

    :param number_dice: Number of dice you wish to roll.
    :precondition:       The argument <number_dice> must be
                         between 1 and 5 (inclusive).
    :postcondition:      Will return a list of length <number_dice>
                         containing random numbers between 1 and 6.
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
    :precondition:      > The argument <scorecard> must be generated
                          from constant function SCORECARD().
                        > The argument <name> must be a string.
    :postcondition:     Will create a player to use in yahtzee()
                        containing attributes necessary for gameplay.
    :return:            Player with attributes.
    """

    pass


def check_multiple_di(roll: list, repetition: int) -> list:

    """
    Check for multiple of the same di in a roll.

    Intended to be used to search for repetition of 3 or greater and
    returns points. If <repetition> number == 5, and a match is
    successful (ie yahtzee), function will always return 50.

    :param roll:         A list of random numbers
    :param repetition:   The repeated value to search for.
    :precondition:       The argument <roll> must be a list of
                         number between 1 and 6.
    :postcondition:      Will perform pattern recognition
                         to detect multiple recurring die
                         in a roll.
    :return:             Regex match (list).
    """

    pass


def check_straight(roll: list, size='small') -> list:

    """
    Check for straight.

    Checks for small or large straight and returns points.
    Keyword argument <size> is set to small by default, but
    can be changed to 'large' to search for a large straight.

    :param roll:    A list of random numbers.
    :param size:    'small' or 'large'
    :precondition:  > The argument <roll> must be a list of
                      numbers between 1 and 6.
                    > User must pass 'small' or 'large' to
                      kwarg <size>.
    :postcondition: Will perform pattern recognition
                    to detect a straight of die
                    in a roll (small or large).
    :return:        Regex match (list).
    """

    pass


def check_number(roll: list, value: int) -> list:

    """
    Check for collection of number.

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
    """

    pass


def check_full_house(roll: list) -> list:

    """
    Check for a full-house and returns points.

    :param roll: A list of random numbers.
    :precondition:  The argument <roll> must be a list of
                    number between 1 and 6.
    :postcondition: Will perform pattern recognition
                    to detect a full house in a roll.
    :return:        Regex match (list).
    """

    pass


def get_available_scores(roll: list, player: dict, scratch=False) -> dict:

    """
    Determine available scores from players held dice.

    Determines and returns the available scores based on
    a player's held dice and the current roll dice. If
    scratch=True, function will return empty score fields
    available to "scratch" out.

    :param roll:    A list of random numbers.
    :param player:  A yahtzee player (dict).
    :param scratch: Boolean which will display available
                    scratch values if set to True.
    :precondition:  > The argument <roll> must be a list of
                      number between 1 and 6.
                    > The argument <player> must be a player
                      instantiated within yahtzee().
    :postcondition: Will perform pattern recognition
                    to detect a full house in a roll.
    :return:        Available scores.
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


def pluck_dice(roll: list, desired_dice: list) -> list:

    """
    Pull dice from roll and pass to player.

    :param roll:            A list of random numbers.
    :param desired_dice:    Dice you wish to pluck from <roll>
    :precondition:          The argument <roll> must be a list of
                            number between 1 and 6.
    :postcondition:         Will place <desired_dice> in a player's
                            attribute "held_dice".
    :return:                A subset of numbers from <roll>.
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

    :param score:   Score to submit to scorecard.
    :param field:   Score field you wish to update.
    :precondition:  Argument <field> must be a valid scorecard key.
    :postcondition: Will update the player's current score.
    :param player:  A yahtzee player (dict).
    """

    pass


def is_bonus(player: dict) -> bool:

    """
    Determine is player is awarded bonus.

    Check if upper section of player's scorecard
    is greater than or equal to 63.

    :param player: A yahtzee player (dict).
    :return: True or False.
    """

    pass


def is_player_done(player: dict) -> bool:

    """
    Determine if player is finished yahtzee.

    Check all scorecard fields to determine if player
    has completed the game.

    :param player:  A yahtzee player (dict).
    :return:        True or False.
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
    """

    pass

