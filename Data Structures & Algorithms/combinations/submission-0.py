class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        visited = set()
        res = []
        def dfs(start, current):
            if len(current) == k:
                res.append(current[:])  # found a valid combination
                return
            for i in range(start, n + 1):
                current.append(i)       # choose i
                dfs(i+1, current)     # recurse with next number
                current.pop()           # un-choose i (backtrack)

        dfs(1,[])
        return res