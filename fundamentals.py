import math
from decimal import Decimal

from common import dsum, dprod, ddiv, km_to_mile_ratio


def is_even(number: int) -> bool:
    return number % 2 == 0


def square_perimeter(a: float) -> Decimal:
    return dprod(4, Decimal(a))


def square_area(a: float) -> Decimal:
    return Decimal(a) ** 2


def rectangle_perimeter(a: float, b: float) -> Decimal:
    return dprod(2, dsum(a, b))


def rectangle_area(a: float, b: float) -> Decimal:
    return dprod(a, b)


def sphere_area(r: float) -> Decimal:
    return dprod(4, math.pi, r ** 2)


def sphere_volume(r: float) -> Decimal:
    return dprod(
        ddiv(4, 3),
        math.pi,
        r ** 3
    )


def km_to_miles(distance: float) -> Decimal:
    return dprod(distance, km_to_mile_ratio)


def pythagorean(a: float, b: float) -> Decimal:
    return Decimal(math.sqrt(dsum(a ** 2, b ** 2)))


def triangle_area(base: float, height: float) -> Decimal:
    return ddiv(dprod(base, height), 2)


def sin_theorem(a: float, b: float, alpha: float) -> Decimal:
    return ddiv(
        dprod(a, b, math.sin(alpha)),
        2
    )


def mean(*args) -> Decimal:
    return ddiv(dsum(*args), len(args))


def geometric_mean(*args) -> Decimal:
    return dprod(*args) ** ddiv(1, len(args))


def harmonic_mean(*args) -> Decimal:
    return ddiv(
        len(args),
        dsum(*[ddiv(1, x) for x in args])
    )


def sum_by_step(start: int, stop: int, step: int) -> int:
    """
    Calculate the sum of numbers between start and stop by stepping with the given value.
    """
    return sum(*[range(start, stop + 1, step)])


def power(base: int, exp: int) -> int:
    prod = 1
    for _ in range(exp):
        prod *= base

    return prod


def sum_of_digits(number: int) -> int:
    return sum([int(x) for x in str(number)])


def is_prime(number: int) -> bool:
    if number <= 0:
        return False

    if number <= 3:
        return True

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def reverse(number: int) -> int:
    return int(str(number)[::-1])


def factorial(number: int) -> int:
    result = 1
    for i in range(1, number + 1):
        result *= i

    return result


def factorial_recursive(number: int) -> int:
    if number == 1:
        return 1

    return number * factorial_recursive(number - 1)


def permutation(n: int, r: int) -> int:
    return factorial(n) // factorial(n - r)


def fibonacci(n: int) -> list:
    if n <= 0:
        return []

    if n <= 2:
        return n * [1]

    result = [1, 1]

    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])

    return result


def nth_fibonacci(index: int) -> int:
    return fibonacci(index)[index - 1]


def nth_fibonacci_recursive(n: int) -> int:
    if n in [1, 2]:
        return 1

    return nth_fibonacci_recursive(n - 1) + nth_fibonacci_recursive(n - 2)


def recursion_series_1(n: int) -> float:
    """
    Calculate the (n / (n + 1)) series.
    """
    if n < 1:
        return 0

    return (n / (n + 1)) + recursion_series_1(n - 1)


def recursion_series_2(n: int) -> float:
    """
    Calculate the (n / (n**2 + 1)) series.
    """
    if n < 1:
        return 0

    return (n / (n ** 2 + 1)) + recursion_series_2(n - 1)


def recursion_series_3(n: int) -> float:
    """
    Calculate the ( (n**2 - 1) / (n**3 + 2) ) series.
    """
    if n < 1:
        return 0

    return ((n ** 2 - 1) / (n ** 3 + 2)) + recursion_series_3(n - 1)
