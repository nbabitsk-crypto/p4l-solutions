def factorial(n:int) -> int:

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

    i = 1  #  this is a counter variable to help keep track of how many multiplicatiosn we've done

    while i <= n:
        p = p*i  #  left side is variable, right side is value
        i = i+1  #  update the counter

#  we are here in the function when i > n
    return p
