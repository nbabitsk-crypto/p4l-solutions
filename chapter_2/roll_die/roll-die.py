import random # this should be helpful!

# Write your roll_die() function here along with any subroutines that you need.
def roll_die() -> int:
    """
    Simulates the roll of a die.
    Parameters:
    - none
    Returns:
    - int: A pseudorandom integer between 1 and 6, inclusively.
    """
    return random.randrange(1,7)
