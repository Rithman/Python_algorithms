# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
import unittest

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))


def max_sum(a, b, c):
    sum_a = sum_b = sum_c = 0
    a_tmp = a
    while a_tmp > 0:
        digit_a = a_tmp % 10
        sum_a += digit_a
        a_tmp //= 10
    b_tmp = b
    while b_tmp > 0:
        digit_b = b_tmp % 10
        sum_b += digit_b
        b_tmp //= 10
    c_tmp = c
    while c_tmp > 0:
        digit_c = c_tmp % 10
        sum_c += digit_c
        c_tmp //= 10
    if sum_a > sum_b:
        if sum_a > sum_c:
            return a, sum_a
        else:
            return c, sum_c
    elif sum_b > sum_c:
        return b, sum_b
    else:
        return c, sum_c


print(max_sum(a, b, c))


class TestDz9(unittest.TestCase):
    def test_max_sum(self):
        self.assertEqual((555, 15), max_sum(222, 555, 333))
