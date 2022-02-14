# Удалить дубликаты из массива "in place".

import unittest


def del_dupl(arr: list) -> list:
    n = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[n]:
            continue
        n += 1
        if n != i:
            arr[n] = arr[i]
    n += 1
    while n < len(arr):
        arr[n] = 0
        n += 1
    return arr


src = [1, 2, 2, 3, 7, 4, 4, 4, 8, 6]

print(del_dupl(src))


class TestDz6(unittest.TestCase):
    def test_del_dupl(self):
        self.assertEqual([1, 2, 3, 7, 4, 8, 6, 0, 0, 0], del_dupl(src))
