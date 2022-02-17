# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Enter number of elements to summarize: '))

row = [1] * n
summ = 1
for i in range(1, n):
    row[i] = row[i - 1] / -2
    summ += row[i]

print(f'Row: {row}')
print(f'Sum: {summ}')
