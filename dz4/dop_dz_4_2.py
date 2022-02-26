
from collections import deque

queue = deque()
queue.append(0)

size, count = map(int, input().split())

for i in range(count):
    arrival, duration = map(int, input().split())
    if queue and [0] <= arrival:
        queue.popleft()

    if len(queue) < size:
        if queue:
            arrival = max(arrival, queue[-1])
        print(arrival)
        queue.append((arrival + duration))
    else:
        print(-1)
