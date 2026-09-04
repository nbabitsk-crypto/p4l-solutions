import math

def sieve_of_eratosthenes(n:int) -> list[bool]:
    """
    Takes an input integer n and returns a list of boolean variables storing the "primaility" of each nonnegative integer up to and including n.
    That is, prime_bools[k] is true if k is prime and false otherwise.
    """

    # assume that everything is prinme and then cross off
    prime_booleans = [True] * (n+1)

    # 0 and 1 can't be pirmne
    prime_booleans[0] = False
    prime_booleans[1] = False

    # range over all integers between 2 and sqrt(n) and cross off their multiple IF they are fray (prime)
    for p in range(2, int(math.sqrt(n)+1)):
        if prime_booleans[p] == True:
            prime_booleans = cross_off_multiples(prime_booleans, p)
    return prime_booleans

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

# Hint: insert your cross_off_multiples() function here
