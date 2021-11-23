"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""


def solution(a, b, k):
    # Eliminate the edge cases first

    # If a equals b that means there is only one number in the range
    # if k is divisible by a, otherwise there is no number in the range
    # case when a, b, k are (0, 0, 11) == 1
    # case when (0, 1, 11) == 0
    if a == b:
        return 1 if a % k == 0 else 0

    # if a and b are different then find a starting point to build the range
    # start from a if it is divisible by k
    # otherwise start from a + remainder of k if k is less than a
    # if k is greater than a, start from k itself
    # even if k is greater than b it doesn't matter since we are going to use range function below
    if a % k == 0:
        start = a
    else:
        start = a + (a % k) if k < a else k

    # build the range and return the length of it
    return len(range(start, b + 1, k))
