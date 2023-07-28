from typing import List


def countdown(start: int) -> None:
    if start:
        print(start)
        countdown(start-1)


def fact1(x: int):
    return x * fact1(x-1) if x else 1


def fact2(x: int, y: int = 1):
    return fact2(x-1, x*y) if x else y


def rec_list_sum(lst: List):
    if len(lst) != 1:
        lst[0] += lst[-1]
        lst.pop(-1)
        rec_list_sum(lst)
    return lst[0]


def rec_lst_sum(lst: List):
    """
    Базовый случай - сумма списка с 1 элементом равна этому элементу
    :param lst:
    :return:
    """
    if len(lst) == 1:
        return lst[0]
    return lst[0] + rec_lst_sum(lst[1:])


def count_elems(lst: List):
    if not lst:
        return 0
    else:
        lst.pop(0)
        return 1 + count_elems(lst)


def find_max_value(lst: List):
    if len(lst) == 1:
        return lst[0]
    else:
        lst_0 = lst.pop(0)
        return lst_0 if lst_0 > find_max_value(lst) else find_max_value(lst)
