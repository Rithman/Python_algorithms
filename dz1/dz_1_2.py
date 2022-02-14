# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import unittest


def letters(char1: str, char2: str) -> str:
    if (ord(char1) and ord(char2)) >= 65 and (ord(char1) and ord(char2)) <= 122:
        char1_pos = ord(char1.upper()) - 64
        char2_pos = ord(char2.upper()) - 64
    elif (ord(char1) and ord(char2)) >= 1040 and (ord(char1) and ord(char2)) <= 1103:
        char1_pos = ord(char1.upper()) - 1039
        char2_pos = ord(char2.upper()) - 1039

    return f'1st letter position: {char1_pos}. 2nd letter position: {char2_pos}. Distance: {abs(char1_pos - char2_pos)}'


class TestDz2(unittest.TestCase):
    def test_letters(self):
        self.assertEqual('1st letter position: 1. 2nd letter position: 26. Distance: 25', letters('a', 'Z'))
        self.assertEqual('1st letter position: 1. 2nd letter position: 32. Distance: 31', letters('А', 'я'))
        self.assertEqual('1st letter position: 6. 2nd letter position: 11. Distance: 5', letters('F', 'k'))

# Не реализовал ввод букв пользователем с консоли т.к. используется unittest
