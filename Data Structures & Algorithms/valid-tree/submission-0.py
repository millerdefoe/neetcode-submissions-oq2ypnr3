class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)

        visited = set()

        def dfs(n, par):
            if n in visited: 
                return False


            visited.add(n)

            for nei in adjMap[n]:
                if nei == par:
                    continue
                if not dfs(nei, n):
                    return False
            return True
            
        return dfs(0, -1) and len(visited) == n