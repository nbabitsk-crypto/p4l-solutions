def min_integers(*numbers: int) -> int:
     # numbers is a tuple
    if len(numbers) == 0:
         raise ValueError("No values given to function.")

    m = numbers[0]

    for val in numbers:
         if val < m:
              m = val

    return m
