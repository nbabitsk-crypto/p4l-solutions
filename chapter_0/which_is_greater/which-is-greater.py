def which_is_greater(x:int, y: int) -> int:
    """
    Takes two integers as input and returns 1 if the first one is larger, 0 if they're equal, and -1 if the second one is larger.
    Parameters:
    - x (int)
    - y (int)
    
    Returns:
    int: 1 if x>y, -1 if x<y, 0 if x=y
    """
    if x == y:
        return 0
    elif x > y:
        return 1
    else:  # we know here that x < y
        return -1
