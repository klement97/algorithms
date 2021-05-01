from decimal import Decimal

km_to_mile_ratio = 0.62137119223


def dsum(*args) -> Decimal:
    if not args:
        raise ValueError('Missing required arguments')

    return sum([Decimal(x) for x in args])


def dprod(*args) -> Decimal:
    if not args:
        raise ValueError('Missing required arguments')

    prod = Decimal(1)
    for arg in args:
        prod *= Decimal(arg)

    return prod


def ddiv(dividend, divisor) -> Decimal:
    if not (dividend and divisor):
        raise ValueError('Missing required arguments')

    return Decimal(dividend) / Decimal(divisor)


def swap_list(lst: list, i: int, j: int):
    lst[i], lst[j] = lst[j], lst[i]
