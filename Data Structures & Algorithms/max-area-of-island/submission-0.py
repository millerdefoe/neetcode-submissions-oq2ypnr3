class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        islandSize = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c)->int:
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            size = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    
                    nrow, ncol = row + dr, col + dc
                    if (nrow in range(ROWS) and
                       ncol in range(COLS) and
                       grid[nrow][ncol] == 1 and
                       (nrow, ncol) not in visited):
                        q.append((nrow, ncol))
                        visited.add((nrow, ncol))
                        size += 1
            return size

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    islandSize = max(bfs(r, c), islandSize)
        
        return islandSize


                    