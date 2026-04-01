class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    nrow, ncol = row + dr, col + dc
                    if nrow in range(ROWS) and ncol in range(COLS) and grid[nrow][ncol] == "1" and ((nrow, ncol) not in visit):
                        q.append((nrow, ncol))
                        visit.add((nrow, ncol))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands



        