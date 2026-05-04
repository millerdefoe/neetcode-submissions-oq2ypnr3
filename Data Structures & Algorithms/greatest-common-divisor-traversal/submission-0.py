class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.components = n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return
        elif self.size[px] > self.size[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]
        self.components -= 1
        return


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        pf_to_numindex = {}

        for i, num in enumerate(nums):
            if num < 2:
                continue
            
            n = 2
            while n * n <= num:
                if num % n == 0:
                    if n in pf_to_numindex:
                        uf.union(i, pf_to_numindex[n])
                    else:
                        pf_to_numindex[n] = i
                    while num % n == 0: 
                        num //= n
                
                n += 1
            if num > 1:
                if num in pf_to_numindex:
                    uf.union(i, pf_to_numindex[num])
                else:
                    pf_to_numindex[num] = i
            
        return uf.components == 1






        