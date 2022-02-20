# В диапазоне натуральных чисел с 2 по 99 определить, сколько из них кратны любому из чисел в диапазоне с 2 по 9.

result = [0] * 8

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            result[j-2] += 1

i = 0
while i < len(result):
    print(i + 2, ' - ', result[i])
    i += 1

