def positive_difference(a: int, b: int) -> int:
    """
    Parameters:
    - a (int)
    - b (int)

    Returns:
    - the absolute value of the difference between a and b
    """
    if a-b > 0:
        return a-b
    else:
        return b-a

        # I must have missed this part of the code along so I came up with this code on my own, but I will ask whether it's the most efficient code I could write during recitation!
