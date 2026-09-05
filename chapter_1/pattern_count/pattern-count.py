def starting_indices(pattern:str, text:str) -> list[int]:
    """
     Finds the occurences that a pettern occurs in a longer text string.
    
        Parameters:
        - pattern (str)
        - text (str): the longer string
    
        Returns:
        list[int]: the collection of starting positions where pattern occurs in text, with overlaps. e.g., "ATA" occurs at positions 0 and 2 in "ATATA".
    """
    k = len(pattern)
    n = len(text)
    count = 0

    if k == 0:
        raise ValueError("empty pattern not allowed.")

    if k > n:
        return 0

    positions = []

    # range over all starting positions, and if I find a match, append it to positions
    for i in range(n-k+1):
        if text[i:i+k] == pattern:
            positions.append(i)

    return positions

def pattern_count(pattern: str, text: str) -> int:
    """
    Finds the number of times that a pettern occurs in a longer text string.

    Parameters:
    - pattern (str)
    - text (str): the longer string

    Returns:
    int: the number of times that pattern occurs in text, with overlaps. e.g., "ATA" occurs twice in "ATATA".
    """
    k = len(pattern)
    n = len(text)
    count = 0

    if k == 0:
        raise ValueError("empty pattern not allowed.")

    if k > n:
        return 0

# if len(text) = n, there are n-k+1 total substrings of length k in a string of length n (range from starting position 0 to n-k)

    return len(starting_indices(pattern, text))
