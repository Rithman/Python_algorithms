# Определить, является ли год, который ввел пользователь, високосным или не високосным.

import unittest


def leap_year(y: int) -> bool:
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        leap_y = True
    else:
        leap_y = False
    return leap_y


class TestDz3(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(True, leap_year(1996))
        self.assertEqual(False, leap_year(1997))
        self.assertEqual(False, leap_year(1))

# Не реализовал ввод года пользователем с консоли т.к. используется unittest
