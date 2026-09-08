# Insert your combination() function here, along with any subroutines that you need.
def combination(n: int, k: int) -> int:
    """
    Compute the combination statistic C(n, k) = n! / ((n - k)! * k!).
    Args:
        n: Total number of distinct objects (non-negative).
        k: Size of the subset to choose (non-negative).
    Returns:
        The number of ways to choose k items from n without order (the binomial coefficient).
    """
    if n < 0 or k < 0:
        raise ValueError("Negative input given to function.")

    def factorial(k: int) -> int:
        """
        Returns the factorial f of an input integer k.
        """
        f = 1
        for i in range (0, k):
            f *= (k-i)
        return f
    
    def permutation(n: int, k: int) -> int:
        """
        Compute the permutation statistic P(n, k) = n · (n-1) · ... · (n-k+1) = n! / (n-k)!.
        Args:
            n: Total number of distinct objects (non-negative).
            k: Number of positions to fill (non-negative).
        Returns:
            The number of ways to choose and order k items from n, i.e., P(n, k).
        """
        if n < 0 or k < 0:
            raise ValueError("Negative input given to function.")
    
        f = 1
        for i in range(1, k+1):
            f *= n-i+1
        
        return f

    # C(n, k) = P(n, k)/k!
    c = permutation(n, k)//factorial(k)
    
    return c
