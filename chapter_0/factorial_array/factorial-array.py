def factorial_array(n: int) -> list[int]:
    """
    Produces a list of all factorials from 0! to n!
    
    Parameters:
    - n (int)
    
    Returns:
    list(int): A list of length n+1 where the k-th element is k!
    """

    if n<0:
            raise ValueError("Error: negative input given.")

    fact = [0]*(n+1)

    fact[0] = 1
    # range through and set k! = k*(k-1)!
    for k in range(1, n+1):
         fact[k] = fact[k-1]*k

    return fact
