import itertools
import random
import re


def VALID_INPUT():

    """
    Return constant VALID_INPUT.

    Copied an adapted from Assignment 2: books.py
    """

    # last element represents "enter" at input()
    return ['pluck', 'remove', 'submit', 'scratch', 'help', 'quit', '']


def MENU():

    """
    Print constant MENU.

    Copied and adapted from Assignment 2: book.py
    Print a list of options at user interface.

    :return: command prompt ('>>>')
    """

    print(
        '====================================================',
        'Press "enter" to roll or choose from the following options:\n',
        f'[1] "{VALID_INPUT()[0]}"\tPluck dice from roll.',
        f'[2] "{VALID_INPUT()[1]}"\tRemove held dice.',
        f'[3] "{VALID_INPUT()[2]}"\tSubmit score.',
        f'[4] "{VALID_INPUT()[3]}"\tScratch score.',
        f'[5] "{VALID_INPUT()[4]}"\tSee usage examples.',
        f'[6] "{VALID_INPUT()[5]}"\tQuit the game.',
        '====================================================',
        sep="\n",
        end="\n"
    )

    return '>>>\t'


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

    fixed_scores = {
        "FULL_HOUSE": 25, "SMALL_STRAIGHT": 30, "LARGE_STRAIGHT": 40,
        "YAHTZEE": 50, "UPPER_BONUS": 35
    }

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
        "small straight": 0, "large straight": 0,
        "yahtzee": 0, "chance": 0
    }

    return scorecard


def yahtzee():

    """
    Run the yahtzee game.

    Front-end function.
    """

    players_done = []
    players = start_game()
    cycle_players = itertools.cycle(players)

    while len(players_done) != len(players):
        player = next(cycle_players)
        print(f'\n{player["NAME"]}s turn!\n')
        pass
        # execute turn
        if is_player_done(player):
            players_done.append(get_final_score(player))


def start_game():

    """
    Get players and start the game.

    Request player names and instantiate yahtzee player objects.
    """

    # pre-loop conditions
    players = []
    number_of_players = ""

    # ask for players until number is entered
    while not number_of_players.isnumeric():
        number_of_players = input("How many players?:\t")

    # generate yahtzee player objects
    for player in range(1, int(number_of_players) + 1):
        name = input(f'What is the name of player {player}?:\t')
        players.append(create_player(name))

    return players


def run_command(command: list, player: dict, roll: list):
    """
    Run user input command.

    Copied and adapted from Assignment 2: Books.py
    Determine user input command to run
    by checking against logical expressions.

    :param command: User input command.
    :param player:  A yahtzee player object.
    :param roll:    A list of ints between 1 and 6.
    :precondition:  Input must be a valid yahtzee command
                    as list of strings.
    :postcondition: Execute the users input command
                    in the yahtzee program.
    """

    # user specifies 'pluck' command
    if command[0] == 'pluck':
        pluck_dice(player, roll, command[1])

    # user specifies 'remove' command
    if command[0] == 'remove':
        remove_dice(player, roll, command[1])

    # user specifies 'submit' command
    if command[0] == "submit":
        submit_score(player, command[1], get_available_scores(roll, player))

    # user specifies 'scratch' command
    if command[0] == "scratch":
        submit_score(player, command[1], get_available_scores(roll, player, scratch=True))

    # user specifies 'quit' command
    if command[0] == 'quit':
        quit('Thanks for playing!')

    # user specifies 'quit' command
    if command[0] == 'help':
        HELP()


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

    # convert list to string
    dice = roll_to_string(roll)

    # build regex argument as string
    repeating_regex_str = r'([1-6])(\1{' + str(repetition-1) + r'})'

    # compile regex object and search
    repeating = re.compile(repeating_regex_str)
    repeating_find = repeating.findall(dice)

    # if repetition equals 5, YAHTZEE
    if repeating_find and repetition == 5:
        return FIXED_SCORES()["YAHTZEE"]

    if repeating_find:
        return sum(roll)

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

    # return 0 if no conditions met
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

    # calculate all available scores
    score_calc = calculate_scores(player, roll)

    # zip keys with calculated scores
    calc_and_keys = zip(score_calc, player["SCORECARD"].keys())

    if scratch:
        available_scores = {key: "scratch" for key in player["SCORECARD"] if player["SCORECARD"][key] == 0}

    else:
        available_scores = {key: value for value, key in calc_and_keys if is_valid_score(player, key, value)}

    return available_scores


def calculate_scores(player, roll):

    """
    Calculate upper and lower scores and return available options.

    :param player:  A yahtzee player object.
    :param roll:    A list of random ints between 1 and 6.
    :precondition:  <player> must be yahtzee player object.
    :postcondition: Will calculate all available scores.
    :return:        Calculated upper and lower scorecard.
    """

    # combine held dice and rolled dice
    dice = sorted(player["HELD_DICE"] + roll)

    # calculate top score sheet from dice
    scoresheet_top = [check_number(dice, number) for number in range(1, 7)]

    # calculate bottom score sheet from dice
    scoresheet_bottom = [
        check_multiple_die(dice, 3), check_multiple_die(dice, 4), check_full_house(dice),
        check_small_straight(dice), check_large_straight(dice), check_multiple_die(dice, 5),
        sum(dice)
    ]

    # get the calculated scores
    return scoresheet_top + scoresheet_bottom


def is_valid_score(player, key, score):

    """
    Determine if score is valid to display.

    :param player: A yahtzee player object.
    :param key: A key in a player's scorecard.
    :param score: A score value
    :return: True or False (bool).
    """

    valid_score = (
            (player["SCORECARD"][key] != "scratch" and score != 0)
            and (player["SCORECARD"][key] == 0 or player["SCORECARD"][key] >= 50)
    )

    return valid_score


def turn(player: dict):

    """
    Execute a turn of yahtzee.

    Helper function for yahtzee().
    Simulates a player's "turn" in yahtzee.

    :param player: A yahtzee player (dict).
    """

    # pre-loop conditions
    turn_count = 0
    roll = roll_dice(5)

    while turn_count != 3:

        # get the input command and parse
        command = format_user_input(input(MENU()).strip())

        # check for invalid syntax
        if is_invalid_syntax(command):
            print("\nINVALID COMMAND\n")

        # check if player ends turn prematurely
        elif is_turn_over(command):
            run_command(command, player, roll)
            player["HELD_DICE"], turn_count = [], 3

        # check if player is out of moves and hasn't ended turn
        elif turn_count == 2 and not is_turn_over(command):
            pluck_dice(player, roll, " ".join(roll_to_string(roll)))

        # commands do not cause turn conditions to change
        elif command[0] in ["help", "pluck", "remove"]:
            run_command(command, player, roll)

        # user has rolled again
        elif command[0] == "":
            roll = roll_dice(5 - len(player["HELD_DICE"]))
            turn_count += 1





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

    return (command[0] == "scratch") or (command[0] == "submit")


def is_invalid_syntax(command: list) -> bool:

    """
    Determine is command at yahtzee prompt is valid.

    Copied and adapted from Assignment 2: books.py

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

    invalid_syntax = command[0] not in VALID_INPUT() or (
                command[0] in VALID_INPUT()[0:4] and len(command) < 2
            )

    return invalid_syntax


def submit_score(player: dict, field: str, available_scores: dict):

    """
    Add score to player scorecard.

    Player can also "scratch" a score if no options are available.

    :param player:              A yahtzee player (dict).
    :param available_scores:    All available scores.
    :param field:               Score field you wish to update.
    :precondition:              <field> must be a valid scorecard key.
    :postcondition:             Update the player's current score.
    """

    # if player submits yahtzee, check for bonus and add score
    if field == "yahtzee" and player['SCORECARD']["yahtzee"]:
        player["SCORECARD"][field] += available_scores[field] * 2

    # otherwise add the score
    elif field in available_scores.keys():
        player["SCORECARD"][field] = available_scores[field]


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

    # get the index of last item in upper card
    end_of_upper_card = list(player["SCORECARD"].keys()).index("sixes")

    # get the upper score values
    upper_score = list(player["SCORECARD"].values())[0:end_of_upper_card+1]

    # get the sum
    upper_sum = sum([score for score in upper_score if str(score) != "scratch"])

    return upper_sum >= 63


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

    # start counter for filled scorecard fields
    fill_count = 0

    # get the scores
    scores = player["SCORECARD"].values()

    for score in scores:
        # if score is scratch or not zero
        if str(score) == "scratch" or score > 0:
            fill_count += 1

    # check if sheet is completely filled
    return fill_count == len(scores)


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

    final_score = sum([score for score in player["SCORECARD"].values() if str(score) != "scratch"])

    if is_bonus(player):
        final_score += FIXED_SCORES()["UPPER_BONUS"]

    return {"NAME": player["NAME"], "final_score": final_score}
