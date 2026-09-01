# functions can also return more than one value
def double_and_duplicate(x: float) -> tuple[float, float]:
    """
    Double the input variable and return two copies of it.

    Parameters:
    - x (float)

    Returns:
    Two copies of 2*x
    """
    return 2*x, 2*x
