def solution(numbers: list[int]):
    numbers = {x for x in numbers if x >= 1}
    if not numbers:
        return 1

    start = 1
    end = start + len(numbers) + 1
    for i in range(1, end):
        if i not in numbers:
            return i
