def find_frequent_words(text: str, k: int) -> list[str]:
    """
    Produces all frequent "k-mers" (substring of length k) in  longer string.

    Parameters:
    - text: str

    Returns:
    list[str]: list of strings representing the most frequent k-mers in text.
    """
    if k<=0:
        raise ValueError("Error: non-positive value of k given to function as input.")

    if k > len(text):
        return[]

    freq_patterns = []

    # generate frequency table of text and k
    freq_map = frequency_table(text, k)

    # what's the maximum value in the table?
    max_val = max_map_value(freq_map)

    # range over frequency table and identify the strings (keys) that achieve the maximum value. When we find one, append it to freq_patterns

    for pattern, val in freq_map.items():
        if val == max_val:
            freq_patterns.append(pattern)

    return freq_patterns
