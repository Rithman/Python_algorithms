class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1

        parents = {i: i for i in range(n)}
        rank = {i: 0 for i in range(n)}

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]

        def merge(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                rank_x = rank[parent_x]
                rank_y = rank[parent_y]
                if rank_x < rank_y:
                    parents[parent_x] = parent_y
                elif rank_x > rank_y:
                    parents[parent_y] = parent_x
                elif rank_x == rank_y:
                    parents[parent_x] = parent_y
                    rank[parent_y] += 1
                return True
            return False

        for k, v in connections:
            if merge(k, v):
                n -= 1
        return n - 1