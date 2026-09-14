def skew_array(genome: str) -> list[int]:
    """
    Returns the skew array for `genome`, where skew[i] is the difference
    (# of 'G') - (# of 'C') in genome[0:i].

    Parameters:
    - genome (str): DNA string.

    Returns:
    - list[int]: Skew array of length len(genome) + 1.

    Raises:
    - ValueError: If genome is empty.
    """
    # TODO: Implement this function

    n = len(genome)
    if n == 0:
        raise ValueError("Empty genome given.")

    # maybe check that it's a valid DNA string (onlyA's, C's, G's, T's)

    skew_array = [0] * (n+1)

    # let's ise a dictionary to help us instead of writing a big if/elif
    skew: dict[str, int] = {
        "A": 0,
        "C": -1,
        "G": 1,
        "T": 0,
    }

    # range over the genome and set skew_array[k]
    for i in range(1, n+1):
        symbol = genome[i-1]

        if symbol in skew:
            # good, add its contribution
            skew_array[i] = skew_array[i-1] + skew[symbol]

    return skew_array

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
    pass
