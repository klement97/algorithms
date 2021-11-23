import cProfile
from datetime import timedelta
from decimal import Decimal
from functools import wraps

from timeit import default_timer

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


def timer(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        end = default_timer()
        print(f'Time: {timedelta(seconds=end - start)}')

        return result

    return wrapper


def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()

        result = func(*args, **kwargs)

        profiler.disable()
        profiler.dump_stats(f"profile.pstat")

        return result

    return wrapper
