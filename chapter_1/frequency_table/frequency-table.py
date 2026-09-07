def frequency_table(text: str, k:int) -> dict[str, int]:
    """
    Generates a "frequency table" mapping k-mer substrings of a text to their numver of occurences.

    Parameters:
    - text: str
    - k: int

    Returns:
    - dict[str, int]: keys are substrings of text having length k, values are number of occurences of that substring
    """

    if k<=0:
        raise ValueError("Error: non-positive value of k given to function as input.")
    if k > len(text):
        return {}

    freq_map: dict[str, float] = {}

    # slide a window along the text of length k
    # (range over all substrings of test of length k)
    n = len(text)

    # how many k-mer substrings of text are there? (n-k+1): starting position 0 up to starting position n-k
    for i in range(n-k+1):
        pattern = text[i:i+k]

        # have I seen pattern before? (Does it exist in the map?)

        # if pattern in freq_map:
                # yes
            # freq_map[pattern] += 1
        # else:
                # add a key-value pair for pattern
           # freq_map[pattern] = 1

        # in python, .get() has two parameters:
        # key, default value to assign the key if not in dictionary
        # it returns existing value if the key is in the sictionary and otherwise creates this key in the sictionary and gives the value given as a parameter.
        freq_map[pattern] = freq_map.get(pattern, 0) + 1

    return freq_map
