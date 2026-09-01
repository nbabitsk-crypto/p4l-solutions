def same_sign(x: int, y: int) -> bool:
    """
    Returns True if two input integers have the same sign and False otherwise.
    
    Parameters:
    - x (int)
    - y (int)
    
    Returns:
    bool: True if x and y have the same sign and False otherwise (zero has the same sign as all integers)
    """
    #  three cases:
    #  1. both positive (x*y >= 0, True)
    #  2. both negative (x*y >= 0, True)
    #  3. opposite signs (x*y <= 0, False)
    return(x*y >= 0)
