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
