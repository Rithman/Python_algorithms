# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

import unittest

number = int(input('Input number: '))
num = int(input('Input digit in number to count: '))


def counter(number, num):
    count = 0
    while number > 0:
        digit = number % 10
        if digit == num:
            count += 1
        number //= 10
    return (count)


class TestDz8(unittest.TestCase):
    def test_counter(self):
        self.assertEqual(6, counter(5551478953255, 5))
