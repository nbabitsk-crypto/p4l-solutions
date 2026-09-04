def reverse_complement(dna: str) -> str:
    """
    Produces the reverse complement of a DNA string (A, C, G, and T symbols only), meaning the string corresponding to a complementary strand.

    e.g., the reverse complement of "AGTC" is "GACT"

    Parameters:
    - dna: str

    OutputL
    str: reverse complement of the input string.
    """
    # dna = complement(dna)  # complement of "AGTC" is "TCAG"
    # dna = reverse(dna)  # reverses the symbols in string
    # return dna
    return reverse(complement(dna))

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
# i    index of s
# 0    n-1
# 1    n-2
# 2    n-3
# i    (n-1)-i
# n-1  0

def complement(dna: str) -> str:
    """
    Finds the complementary strand of a given DNA string without reversing it.
    
    Parameters:
    - dna (str)

    Returns:
    string: the string whose i-th symbol is the complementary nucleotide of the i-th symbol of the inout string (A-T, C-G, T-A, G-C)
    """

    dna2 = ""

    # range over the string, take complement at each position
    # we will use a match statement (called a switch in other languages)
    for symbol in dna:  # this ranges over the symbols
        # what is the current symbol in my string?
        match symbol:
            case "A":
                dna2 += "T"
            case "C":
                dna2 += "G"
            case "G":
                dna2 += "C"
            case "T":
                dna2 += "A"
            case _:
                raise ValueError("Error: symbol in the string is not a DNA nucleotide.")
        
    return dna2
