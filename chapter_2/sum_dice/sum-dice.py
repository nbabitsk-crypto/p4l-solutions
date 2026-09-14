import math
import random # this should be helpful!

def roll_die() -> int:
    """
    Simulates the roll of a die.
    Parameters:
    - none
    Returns:
    - int: A pseudorandom integer between 1 and 6, inclusively.
    """
    return random.randrange(1,7)

def sum_dice(num_dice: int) -> int:
    """
    Simulates the rolling of two dice.
    Parameters:
    - num_dice: int
    Returns:
    - int: A pseudorandom integer corresponding to simulating the roll of num_dice dice and returning their sum.
    """
    total = 0

    # range over number of dice and add one roll's value to the total
    for _ in range(num_dice):
        total += roll_die()

    return total
