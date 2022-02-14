# Удалить дубликаты из массива.

import unittest


def del_dupl(arr: list) -> list:
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result


src = [1, 2, 2, 3, 7, 4, 4, 4, 8, 6]


class TestDz4(unittest.TestCase):
    def test_del_dupl(self):
        self.assertEqual([1, 2, 3, 7, 4, 8, 6], del_dupl(src))
