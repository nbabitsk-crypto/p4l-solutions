import math

def trivial_prime_finder(n:int) -> list[bool]:
    """
    Takes integer n and returns a list of boolean variables storing the "prinmality" of each nonnegative integer up to and including n.

    That is, prime_bools[k] is true if k is prime and false otherwise.
    """
    if n<0:
        raise ValueError("Error:n must be nonnegative.")

    prime_booleans=[False] * (n+1)

    # note: prime_booleans[0] and prime_booleans[1] are noth False, so we don't need to set them

    # range over all the other numbers and check if they're prime
    for p in range(2, n+1):
         prime_booleans[p] = is_prime(p)

    return prime_booleans

def is_prime(p:int) -> bool:
    """
    Takes as input a nonnegative integer k.

    Returns True of K os pprime, and False otherwise.
    """
    if p < 0:
        raise ValueError("Error: k must be nonnegative.")
    if p < 2:
        return False  # 0 and 1 certainly aren't prime

    # try every number between 2 and p-1 as a divisor of p
    # and if we find one that is a divisor, return False
    # note: if a * b = p, then a and b can't both be > sqrt(p), so we only need to check up to sqrt(p)

    for k in range(2, math.isqrt(p)+1):
        if p % k == 0:
            # flip off the light
            return False

    # we survived the challenged and win the game
    return True

    # we survived the challenged and win the game
    # Hint: place your is_prime() subroutine here.
