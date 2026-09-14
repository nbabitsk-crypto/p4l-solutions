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

def min_integer_array(a:list[int]) -> int:
    """"
    Returning the minimum value in a list of integers.
    """

    if len(a) == 0:
        raise ValueError("Error: empty list given.") 

    m = 0

    # iterate over list, updating m if we find a smaller value

    for i, val in enumerate(a):
        # ranges over the values in a list
        # if we find a smaller value than the current min 
        # OR we are at the first element, update m
        if val < m or i == 0:
            m = val

    return m

    # Insert your minimum_skew() function here, along with any subroutines that you need.
def minimum_skew(genome: str) -> list[int]:
    """
    minimum_skew finds the list of integers representing all integer indices that minimizes the skew     of the genome text.
    Parameters:
    - genome (str): A genome string.
    Returns:
    - list[int]: A list of indices that minimize the skew value of the genome text.
    """
    # indices of skew_array that reach value of min_integer_array

    min_vals = []
    s = skew_array(genome)
    m = min_integer_array(s)
    for i in range(len(s)):
        if s[i] == m:
            min_vals.append(i)

    return min_vals
    
def min_window_skew(genome: str, window_len: int) -> list[int]:
    """
    Return all start indices of windows of length window_len in genome
    that achieve the minimum GC-skew.

    Parameters:
        genome (str): A nonempty DNA string consisting of 'A', 'C', 'G', 'T'.
        window_len (int): The length of the window (1 ≤ window_len ≤ len(genome)).

    Returns:
        (list[int]): A list of start indices (0-based) in increasing order 
                   where the window skew is minimal.
                   If window_len > len(genome), return [].
    """
    if window_len > len(genome):
        return []
    # compute the skew of each substring, then find the minimum, then find indices where that min occurs
    list_skews = []
    for i in range(0, len(genome)-window_len+1): # range over all windows
        arr = skew_array(genome[i:i+window_len]) # find the skew of each window
        list_skews.append(arr[window_len]) # make the list of skews

    gen_min = min_integer_array(list_skews) # this is the min skew value, now i have to find indices where it occurs
    min_indices = []
    for i in range(0, len(genome)-window_len+1):
        arr = skew_array(genome[i:i+window_len])
        if arr[window_len] == gen_min:
            min_indices.append(i)
    return min_indices
