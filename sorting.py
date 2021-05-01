from common import swap_list


def selection_sort(lst: list) -> list:
    list_len = len(lst)

    for i in range(list_len - 1):
        for j in range(i + 1, list_len):
            if lst[j] < lst[i]:
                swap_list(lst, i, j)

    return lst


def insertion_sort(lst: list) -> list:
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            swap_list(lst, j - 1, j)
            j -= 1

    return lst
