from typing import List


class SelectionSort:

    def __init__(self, iterable: List):
        self.iterable = iterable

    def _find_smallest_index(self):
        smallest = self.iterable[0]
        smallest_index = 0
        for i, j in enumerate(self.iterable):
            if j < smallest:
                smallest = j
                smallest_index = i
        return smallest_index

    def sort(self):
        sorted_iterable = []
        for _ in range(len((self.iterable))):
            smallest_index = self._find_smallest_index()
            sorted_iterable.append(self.iterable.pop(smallest_index))

        return sorted_iterable


ss = SelectionSort([2, 4, 7, 56, 3, 5, 2, 51, 1])


