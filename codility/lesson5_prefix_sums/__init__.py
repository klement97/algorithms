from collections import defaultdict


def prefix_sum(array):
    lookup = defaultdict(lambda: 0)

    for i in range(1, len(array) + 1):
        lookup[i] = lookup[i - 1] + array[i - 1]

    return lookup
