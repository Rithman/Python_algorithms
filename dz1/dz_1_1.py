# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

import unittest


def summ_of_digits(num: int) -> int:
    summ = 0
    while num > 0:
        digit = num % 10
        summ += digit
        num //= 10
    return summ


def mult_of_digits(num: int) -> int:
    mult = 1
    while num > 0:
        digit = num % 10
        mult *= digit
        num //= 10
    return mult


class TestDz1(unittest.TestCase):
    def test_summ(self):
        self.assertEqual(6, summ_of_digits(123))
        self.assertEqual(0, summ_of_digits(000))

    def test_mult(self):
        self.assertEqual(6, mult_of_digits(123))
        self.assertEqual(0, mult_of_digits(120))
