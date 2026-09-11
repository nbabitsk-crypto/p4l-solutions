# Insert your max_integer_array() function here, along with any subroutines that you need.
def max_integer_array(lst: list[int]) -> int:
    """
    Return the maximum integer in a non-empty list.
    Args:
        lst: A non-empty list of integers.
    Returns:
        The largest integer in lst.
    """
    k = lst[0]  # k contains the current largest integer
    for i in range(1, len(lst)):
        if lst[i] > k:
            k = lst[i]
    return k
