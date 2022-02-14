# Переместить все нули в массиве назад, сохранив относительный порядок остальных элементов.

import unittest


def move_zero(arr: list) -> list:
    n = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[n] = arr[i]
            n += 1
    while n < len(arr):
        arr[n] = 0
        n += 1
    return arr


arr = [4, 1, 0, 2, 0, 3, 6, 0, 9, 7, 0]


class TestDz5(unittest.TestCase):
    def test_move_zero(self):
        self.assertEqual([4, 1, 2, 3, 6, 9, 7, 0, 0, 0, 0], move_zero(arr))
