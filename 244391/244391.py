import sys

# Please do not remove package declarations because these are used by the autograder. 
# If you need additional packages, then you may declare them above.


# Insert your collatz(n) function here, along with any subroutines that you need.
# The function should return a list of the terms in a collatz sequence from n to 1.

def collatz(n: int) -> list:
    if n <= 0:
        return ValueError("Function given a non-positive integer.")

    list = []
    list.append(n)
    while n != 1:
        if n%2 == 0:
            n = n/2
            list.append(n)
        else: 
            n = 3*n + 1
            list.append(n)
   
    return list
