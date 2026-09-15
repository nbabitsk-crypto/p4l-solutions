def at_skew_array(genome: str) -> list[int]:
    """
    Compute the AT skew array of a genome string.

    Parameters:
        genome (str): A DNA string consisting of 'A', 'C', 'G', 'T' (case-insensitive).

    Returns:
        list[int]: The AT skew array, starting with 0, where each subsequent
                   value is the previous value plus +1 for 'A', -1 for 'T',
                   and 0 otherwise.
    """
    skew = [0]

    for i in range(len(genome)):
        if genome[i] == "A":
            skew.append(skew[i]+1)
        elif genome[i] == "T":
            skew.append(skew[i] - 1)
        else:
            skew.append(skew[i] + 0)
    return skew
