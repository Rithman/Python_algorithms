# Реализация кучи как на лекции

def get_parent(index):
    return (index - 1) // 2


def get_left(index):
    return index * 2 + 1


def get_right(index):
    return index * 2 + 2


class Heap:
    def __init__(self):
        self.array = []

    def sift_down(self, index):
        min_index = index
        left = get_left(index)
        right = get_right(index)
        if left < len(self.array) and self.array[left] < self.array[min_index]:
            min_index = left
        if right < len(self.array) and self.array[right] < self.array[min_index]:
            min_index = right

        if index != min_index:
            self.array[index], self.array[min_index] = self.array[min_index], self.array[index]
            self.sift_down(min_index)

    def sift_up(self, index):
        while index > 0 and self.array[get_parent(index)] > self.array[index]:
            self.array[index], self.array[get_parent(index)] = self.array[get_parent(index)], self.array[index]
            index = get_parent(index)

    def add(self, val):
        self.array.append(val)
        self.sift_up(len(self.array) - 1)

    def extract_min(self):
        min = self.array[0]

        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        self.array.pop()
        self.sift_down(0)

        return min

    def get_size(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)


# Параллельная обработка
# Я не знаю, что за проклятие на мне лежит, но у меня опять не принимает input на Степике.
# Сам код на примерах из комментариев работает правильно.

queue = Heap()
n, m = map(int, input().split())

for i in range(n):
    queue.add([0, i])

for task in range(m):
    time = int(input())
    curr = queue.extract_min()
    print(*reversed(curr))
    curr[0] += time
    queue.add(curr)
