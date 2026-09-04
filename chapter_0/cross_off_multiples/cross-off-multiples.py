def cross_off_multiples(prime_booleans:list[bool], p:int) -> list[bool]:
    """
    Takes as input a list of booleans representing the primality of all integers up to some point
    
    Also takes as input an integer p.
    
    Updates the list by setting to False all idices in the list that are multuples of p (starting at 2*p)
    """
    n = len(prime_booleans) - 1

    # range ofver multiples
    for i in range (2*p, n+1, p):
        prime_booleans[i] = False  # "cross off" current number because I know that i is a multiple of p
        
    return prime_booleans
