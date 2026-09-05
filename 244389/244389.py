import sys

# Please do not remove package declarations because these are used by the autograder.
# You may declare additional packages above if needed.


# Insert your isAmicable(a, b) function here, along with any subroutines that you need.
# The function should return a boolean: True if (a, b) are amicable, otherwise False.
def isAmicable(a: int, b: int) -> bool:
    if sum_divisors(a) == b:
        return True
    elif sum_divisors(b) == a:
        return True
    return False
    
def sum_divisors(n:int) -> int:
    l = proper_divisors(n)
    s = 0

    for i in range(0, len(l)):
        s += l[i]
    return s


def proper_divisors(n:int) -> list:
    list_divisors = []
    for i in range(1, n):  # not including n, because we are looking for divisors < n
        if n%i == 0:  # if i is a perfect divisor of n
            list_divisors.append(i)  #  add 1 to the count
    return list_divisors

    return 42
