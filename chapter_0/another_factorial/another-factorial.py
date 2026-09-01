def another_factorial(n:int) -> int:

    """
    Produces n! = n*(n-1)*...(2)*1

    Parameters:
    - n (int)

    Returns:
    int: n!

    Raises an error if n < 0.
    """
    if n < 0:
        #  handle the negative input with an error
        raise ValueError("Error: negative input given to factorial.")
    p = 1  #  think of p as the container that will represent my growin product

    # range(a,b) in Python represents the integers between a and b-1 inclusively

    # for every integer i between 1 and n, p = p*i
    for i in range(1, n+1):  #  adds 1 to i automatically
        p = p*i  #  left side is variable, right side is value

#  we are here in the function when i > n
    return p
