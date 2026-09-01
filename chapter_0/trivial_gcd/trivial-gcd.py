def trivial_gcd(a: int, b: int) -> int:
    """
    Returns the GCD of two input integers a and b.
    Implement the "trivial" approach that is what humans are taught to do when computing a GCD by hand, trying every possible divisor.
    """
    d = 1
    m = min(a, b)
    for p in range(1, m+1):
        # how do I check that p is a divisor of both a and b?
        if (a % p == 0) and (b % p == 0):
            # I can only be here if p is a divisor of both 
            d = p
    return d
