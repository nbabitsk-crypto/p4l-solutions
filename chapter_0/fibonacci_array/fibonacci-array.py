# Insert your fibonacci_array() function here, along with any subroutines that you need.
def fibonacci_array(n: int) -> list[int]:
    """
    Return an array of Fibonacci numbers from F₀ through Fₙ.
    Args:
        n: A non-negative integer.
    Returns:
        A list F of length n + 1 such that F[k] is the k-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("Negative input given to function.")
    F = [1]  # supposed to come out to 1, 1, 2, 3, 5, 8, 13, 21, ...
    if n >= 1:
        F.append(1)
    for i in range(2, n+1):
        F.append(F[i-2]+F[i-1])  # add the last two integers to get the next one
# F = [ 1, 1, 2, 3] yayy! i solved it :)

    return F
