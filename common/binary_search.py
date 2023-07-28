from typing import Optional
"""
* log n == log_2(n)
О-большое описывает скорость работы алгоритма количеством операций в худшем случае
Простой поиск среди n отсортированных элементов: O(n) - линейное
Бинарный поиск среди n отсортированных элементов: O(log n)
"""


def binary_search(iterable, search_goal) -> Optional[int]:
    """
    :param iterable: sorted asc iterable
    :param search_goal: desired iterable element
    :return: index of desired element or None
    """
    left_border = 0
    right_border = len(iterable)
    steps = 0
    while left_border <= right_border:
        middle = (right_border + left_border) // 2
        steps += 1
        print(f"[step {steps}]: {left_border}---{middle}---{right_border}")
        if iterable[middle] < search_goal:
            left_border = middle + 1
        elif iterable[middle] > search_goal:
            right_border = middle - 1
        else:
            return middle


if __name__ == "__main__":
    iterable = [i for i in range(0, 128, 1)]

    print(binary_search(iterable, 0))
