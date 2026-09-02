def sum_of_squares(n: int) -> int:
    """
    Calculate the sum of squares from 1^2 + 2^2 + ... + n^2.

        Parameters: 
        n (int) - The upper bound of the sum (must be >= 1). 

    Returns: 
        total (int) - The sum of the squares from 1 to n.
    """
    k = 0
    for i in range(1, n+1):
        k = k + i**2
    return k
