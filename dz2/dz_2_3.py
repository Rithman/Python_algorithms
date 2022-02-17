# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843. (Сделать без использования строк)

import unittest


def reverse_num(num: int):
    rev_num = 0
    while num > 0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num //= 10
    return rev_num


class TestDz3(unittest.TestCase):
    def test_reverse_num(self):
        self.assertEqual(54321, reverse_num(12345))
        self.assertEqual(99999, reverse_num(99999))
        self.assertEqual(0, reverse_num(0000))