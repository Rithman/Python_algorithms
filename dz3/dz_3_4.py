# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import unittest


def two_min_in_array(arr: list):
    if arr[0] < arr[1]:
        min_1 = 0
        min_2 = 1
    else:
        min_2 = 0
        min_1 = 1

    for i in range(2, len(arr)):
        if arr[i] < arr[min_2]:
            tmp = min_2
            min_2 = i
            if arr[tmp] < arr[min_1]:
                min_1 = tmp
        elif arr[i] < arr[min_1]:
            min_1 = i

    return arr[min_1], arr[min_2]


class TestDz4(unittest.TestCase):
    def test_tow_min_in_array(self):
        self.assertEqual((-5, 2), two_min_in_array([-5, 32, 3, 5, 7, 11, 15, 16, 6, 2]))
        self.assertEqual((2, 2), two_min_in_array([9, 32, 3, 5, 7, 11, 15, 2, 6, 2]))
