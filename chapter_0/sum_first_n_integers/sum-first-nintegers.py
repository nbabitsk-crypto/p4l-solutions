def sum_first_n_integers(n: int) -> int:
    """
    Sums the first n positive integers.
    
    Parameters:
    - n (int)
    
    Returns:
    int: Sum of the first n positive integers.

    Raises an error if n < 0.
    """
    if n < 0:
        #  handle negative input with an error
        raise ValueError("Error: negative input given to sum_first_n_integers().")
    
    p = 0  #  stores the value of the ongoing sum
    i = 1  #  holds the value of the next integer we will add

    while i <= n:
        p += i  #  this is shorthand for s = s + 1
        i += 1  #  shorthand for i = i + 1 (Python doesn't have i++)

    # also: s *= i, s /= i, s-= i

    #  at this point, we know that i > n

    return p
