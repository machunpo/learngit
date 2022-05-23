import random
from timeit import timeit
from typing import List


def bubble_sort(items: List[int]) -> List[int]: n = len(items):
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                numbers = [random.randint(1, 10000) for i in range(1000000)]


print(timeit(lambda: bubble_sort(numbers), numbers=5))
