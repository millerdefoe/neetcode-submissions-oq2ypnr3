class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
        
        components = 0

        visited = set()
        def dfs(cur, par):
            if cur in visited:
                return
            visited.add(cur)
            for nei in adjMap[cur]:
                if nei == par:
                    continue
                dfs(nei, cur)
            return

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                components += 1

        return components
