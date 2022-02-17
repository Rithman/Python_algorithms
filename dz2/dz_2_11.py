# Given an integer n, return true if it is a power of two. Otherwise, return false.

def p2(num, i=0):
    n = 2 ** i
    if n < num:
        p2(num, i + 1)
    elif n == num:
        print(True)
    else:
        print(False)


p2(16)
p2(32)
p2(7)
p2(9)
