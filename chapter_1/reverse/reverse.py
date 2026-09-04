def reverse(s: str) -> str:
    """
    Reverses the symbols in an input string

    Parameters:
    - s: str

    Returns:
    str: the reverse of s
    """
    characters = []
    rev = ""

    n = len(s)

    for i in range (n):
        characters.append(s[n-1-i])

    # now we need to convert this list to a string
    return "".join(characters)
