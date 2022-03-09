from random import randint


def median(arr: list) -> int:

    base = arr[0]

    less_list = []
    more_list = []
    less_count = 0
    more_count = 0

    for elem in array:
        if elem < base:
            less_count += 1
        elif elem > base:
            more_count += 1

        if elem in arr:
            if elem < base:
                less_list.append(elem)
            elif elem > base:
                more_list.append(elem)

    if less_count > more_count:
        return median(less_list)
    elif less_count < more_count:
        return median(more_list)

    return base


m = randint(0, 10)
array = []

for num in range(2 * m + 1):
    x = randint(0, 100)
    array.append(x)

print(f'm: {m}')
print(f'Array: {array}')
print(f'Median: {median(array)}')
