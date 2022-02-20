# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


arr = [6, -3, 5, 7, -2, 1, -4, 6, 2, -7, 10]


def min_val(arr: list):
    min_val = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val


max_negative = min_val(arr)

for i in range(len(arr)):
    if arr[i] < 0:
        if arr[i] > max_negative:
            max_negative = arr[i]

print(max_negative)

