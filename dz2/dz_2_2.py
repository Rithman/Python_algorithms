# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import unittest


def count(num: int):
    even = 0
    not_even = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0 or digit == 0:
            even += 1
        else:
            not_even += 1
        num //= 10
    return (f'Even count: {even}; Not Even count: {not_even}')


class TestDz2(unittest.TestCase):
    def test_count(self):
        self.assertEqual('Even count: 4; Not Even count: 5', count(598650198))
        self.assertEqual('Even count: 0; Not Even count: 7', count(9999999))
        self.assertEqual('Even count: 5; Not Even count: 1', count(100000))
