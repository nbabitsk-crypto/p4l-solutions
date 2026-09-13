import math

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
# Insert your list_mersenne_primes() function here, along with any subroutines that you need.
def list_mersenne_primes(n: int) -> list[int]:
    """
    List all Mersenne primes of the form 2^p - 1 with p ≤ n.
    Args:
        n: Upper bound on the exponent p (non-negative integer).
    Returns:
        A list of all primes of the form 2^p - 1 where p is prime and p ≤ n,
        in increasing order of p.
    """
    if n < 0:
        raise ValueError("Given upper bound is negative.")

    list_primes = []

    for p in range(n+1):
        if is_prime(p) and is_prime(2**p - 1):
            list_primes.append(2**p - 1)
    return list_primes
