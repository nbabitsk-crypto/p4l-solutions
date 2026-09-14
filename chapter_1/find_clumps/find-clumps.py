def main():
    print("Finding clumps.")

# Pseudocode from the learning objectives (for reference)

"""
FindClumps(text, k, L, t)
    patterns ← an array of strings of length 0
    n ← length(text)
    for every integer i between 0 and n − L
        window ← text[i, i + L]
        freqMap ← FrequencyTable(window, k)
        for every key s in freqMap
            if freqMap[s] ≥ t and Contains(patterns, s) = false
                patterns ← append(patterns, s)
    return patterns
"""

# text = "BANANASPLIT"
# window_length = 6
# k = 3
# first window:
#    "BAN" 1
#    "ANA" 2
#    "NAN" 1

# second window: ANANAS
# "ANA"  2
# "NAN"  1
# "NAS"  1

def find_clumps_faster(text: str, k: int, window_length: int, t: int) -> list[str]:
    """
    Finds a list of strings representing all k-mers that appear at least t times
    in a window of given length in the string.

    Parameters:
    - text (str): The input string.
    - k (int): The k-mer length.
    - window_length aka L (int): Length L of the sliding window.
    - t (int): Frequency threshold within a window.

    Returns:
    - list[str]: All distinct k-mers forming (L, t)-clumps in text.

    Notes:
    - Follow the FindClumps pseudocode above.
    - Build a frequency table for each window using `frequency_table`.
    - Avoid duplicates by checking `s not in patterns` before appending.
    """
    # think about all the checks that you would want to do about the paraneters
  
    if len(text) ==0:
        raise ValueError("Empty string.")

    if k > window_length:
        raise ValueError("k too big.")

    n = len(text)

    if t < 0 or k < 0 or n < 0:
        raise ValueError("Negative input given.")

def find_clumps(text: str, k: int, window_length: int, t: int) -> list[str]:
    """
    Finds a list of strings representing all k-mers that appear at least t times
    in a window of given length in the string.

    Parameters:
    - text (str): The input string.
    - k (int): The k-mer length.
    - window_length aka L (int): Length L of the sliding window.
    - t (int): Frequency threshold within a window.

    Returns:
    - list[str]: All distinct k-mers forming (L, t)-clumps in text.

    Notes:
    - Follow the FindClumps pseudocode above.
    - Build a frequency table for each window using `frequency_table`.
    - Avoid duplicates by checking `s not in patterns` before appending.
    """
    # think about all the checks that you would want to do about the paraneters
  
    if len(text) ==0:
        raise ValueError("Empty string.")

    if k > window_length:
        raise ValueError("k too big.")

    n = len(text)

    if t < 0 or k < 0 or n < 0:
        raise ValueError("Negative input given.")

    patterns: list[str] = []  # will store our frequent k-mers

    # range over all the windows!
    # a string of length n has how many substrings of length window_length? n - window_length + 1\
    for i in range(n - window_length + 1):
        window = text[i:i+window_length]
        freq_map = frequency_table(window, k)

        # what are the patterns that appear at least t times in my freq_map AND that don't already occur in patterns?
        for s, val in freq_map.items():
            if val >= t and not (s in patterns):
                # this is the type of string that I am looking for
                patterns.append(s)

    for i in range(n - window_length + 1):
        if i%1000 == 0:
            print("Hi, I'm on starting position", i)

    return patterns


def frequency_table(text: str, k: int) -> dict[str, int]:
    """
    Builds a frequency table of all k-mers of length k in the given text, 
    including overlaps.
    
    Parameters:
    - text (str): The input string.
    - k (int): The size of the k-mers.
    
    Returns:
    - dict[str, int]: A dictionary mapping each k-mer to its frequency.
    """
    if k <= 0:
        raise ValueError("k is not positive.")
    if k > len(text):
        return {}

    # declare a blank map
    freq_map: dict[str, int] = {}

    n = len(text)

    # range over all k-mer substrings of text
    for i in range(n-k+1):
        # grab current pattern of length k
        pattern = text[i:i+k]

        # does pattern exist in freq_map??
        # if not, then we create it as an entry 

        """
        CLASSIC WAY
        if pattern not in freq_map:
            freq_map[pattern] = 1
        else:
            # we have seen it!
            freq_map[pattern] += 1
        """

        # shortcut approach using get() 
        # get() takes two parameters: the key to retrieve, and a default value to assign it if it doesn't exist as a key
        freq_map[pattern] = freq_map.get(pattern, 0) + 1


    return freq_map

if __name__ == "__main__":
    main()
