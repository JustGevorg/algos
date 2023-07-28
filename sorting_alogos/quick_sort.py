from typing import List
import random


def dummy_quick_sort(lst: List):
    """Опорный элемент - первый"""
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]

        return dummy_quick_sort(less) + [pivot] + dummy_quick_sort(greater)


def quick_sort(lst: List):
    """Опорный элемент - случайный"""
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[random.randint(0, len(lst)-1)]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    print(quick_sort([9, 10, 1, 3, 11, 2, 0]))
