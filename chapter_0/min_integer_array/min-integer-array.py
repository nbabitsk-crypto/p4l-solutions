def  min_integer_array(a: list[int]) -> int:
    if len(a) == 0:
        raise ValueError("Error: empty list given to function.")

    m = a[0]  # stores our minimum

    for val in a:
         # is the current value better than what I currently have?
         if val < m:
              # update m appropriately
              m = val

    return m
