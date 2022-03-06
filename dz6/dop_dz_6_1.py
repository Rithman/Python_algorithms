from collections import deque


class Solution:

    def connect(self, root):
        if not root:
            return root
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if i == (size - 1):
                    curr.next = None
                else:
                    curr.next = queue[0]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return root
