class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()


        def dfs(r,c):
            if r == ROWS or r < 0 or c == COLS or c < 0:
                return

            if grid[r][c] == "0":
                return
            
            if (r,c) in visited:
                return
            visited.add((r,c))
            
            directions = {(1,0),(0,1),(-1,0),(0,-1)}

            for d in directions:
                dfs(r+d[0],c+d[1])

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1

        return islands