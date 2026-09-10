# Insert your prefixes() function here.
def prefixes(s: str) -> list[str]:
    """
    Return a list of all prefixes of the string s.

    Parameters:
        s (str) - The input string.

    Returns:
        list[str] - A list of prefixes of s, starting with the empty string ""
                    and ending with s itself.
    """
    prefix_list = []
    # prefixes = s[i:i+k], where k increases by 1 until the end of the word
    for k in range(len(s)+1):
        prefix_list.append(s[0:k])
    return prefix_list
