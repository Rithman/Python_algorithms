from collections import deque


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        queue = deque()
        queue.append(root)
        parent_list = {root: None}
        while p not in parent_list or q not in parent_list:
            curr = queue.pop()
            if curr.left:
                parent_list[curr.left] = curr
                queue.append(curr.left)
            if curr.right:
                parent_list[curr.right] = curr
                queue.append(curr.right)

        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent_list[p]

        while q not in ancestors:
            q = parent_list[q]

        return q
