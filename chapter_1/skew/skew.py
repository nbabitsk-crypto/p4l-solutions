def skew(symbol: str) -> int:
    """
    Returns 1 if symbol is 'G'/'g', -1 if 'C'/'c', else 0.

    Parameters:
    - symbol (str): Single-character string.

    Returns:
    - int: Skew contribution for this symbol.

    Raises:
    - ValueError: If `symbol` is not length 1.
    """
    # TODO: Implement this function
    skew: dict[str, int] = {
        "A": 0,
        "C": -1,
        "G": 1,
        "T": 0,
    }
    if symbol in skew:
        return skew[symbol]
    return 0
