def sum_even(k: int) -> int:
    """
    Sums all the even positive integers up to, and possibly including, k.
    
    Parameters:
    - k: int
    
    Returns:
    - int: sum of the even positive integers up to k.
    """
    if k < 0:
        raise ValueError("Error: Negative k given to function.")

    s = 0

    for i in range(2, k+1, 2):
        s += i
    return s
