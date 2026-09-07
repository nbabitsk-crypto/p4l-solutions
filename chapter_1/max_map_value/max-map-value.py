def max_map_value(map: dict[str, int]) -> int:
    """
    Finds the maximum value in an input dictionary mapping strings to integers.
    """
    if len(map) == 0:
        raise ValueError("Error: empty map given.")

    
    # range through the integers in the dictionary
    # if the integer value in the dictionary is greater than the current max_val, update max_val to be equal to that number

    vals = list(map.values())
    m = vals[0]

    for val in vals:
        if val > m:
            m = val

    return m

    # for current_value in map.values():
        # if current_value > max_val:
            # max_val = current_value
    # return max_val

    print(max_map_value(map))
