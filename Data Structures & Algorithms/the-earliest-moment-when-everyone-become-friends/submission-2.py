class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = list(range(n))
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return 0
        else:
            if self.rank[px] >= self.rank[py]:
                self.parent[py] = px
                self.rank[px] += self.rank[py]
                if self.rank[px] == len(self.rank):
                    return 1
            else:
                self.parent[px] = py
                self.rank[py] += self.rank[px]
                if self.rank[py] == len(self.rank):
                    return 1

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        earliest_time = -1
        uf = UnionFind(n)

        logs.sort(key = lambda x : x[0])

        for log in logs:
            if uf.union(log[1], log[2]) == 1:
                earliest_time = log[0]
        
        return earliest_time








