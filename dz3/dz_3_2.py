# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

arr = [9, 3, 5, 7, 2, 1, 4, 6, 2]


def max_val(arr: list):
    max_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


def min_val(arr: list):
    min_val = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val


max_val = max_val(arr)
min_val = min_val(arr)

for i in range(len(arr)):
    if arr[i] == max_val:
        arr[i] = min_val
    elif arr[i] == min_val:
        arr[i] = max_val

print(arr)
