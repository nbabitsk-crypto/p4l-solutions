# Insert your sum_proper_divisors() function here, along with any subroutines that you need.
def sum_proper_divisors(n: int) -> int:
    """
    Return the sum of all proper (positive) divisors of n, i.e., divisors strictly less than n.
    Args:
        n: Integer input.
    Returns:
        The sum of all positive divisors of n that are < n.
        Returns 0 for n <= 1.
    """
    if n <= 1:
        return 0
        
    s = 0 # running total value of the proper divisors
    for i in range(1, n):  # not including n, because we are looking for divisors < n
        if n%i == 0: # if i is a perfect divisor of n
            s += i

    return s
