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
