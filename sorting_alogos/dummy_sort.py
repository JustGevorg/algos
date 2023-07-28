from typing import List


def dummy_sort(iterable: List):
    """
    Сложность O(n*n) из-за двух проходов по списку
    """
    sorted_iterable = []
    iterable_len = len(iterable)
    for i in range(iterable_len):
        max_el = iterable[0]
        for j in iterable:
            if j > max_el:
                max_el = j
        sorted_iterable.append(max_el)
        iterable.remove(max_el)
    return sorted_iterable
