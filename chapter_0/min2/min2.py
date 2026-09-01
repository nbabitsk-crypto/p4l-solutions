def min_2(a: int, b: int) -> int:
    """
    Takes two integers and returns their minimum
    
    Parameters:
    - a (int)
    - b (int)

    Returns:
    int: minimum of a and b
    """
    if a < b:
        return a  #  a is smaller
    else:  #  b is greater than or equal to a
        return b
