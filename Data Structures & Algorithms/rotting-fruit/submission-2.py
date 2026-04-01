class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 100% BFS
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        q = deque()
        time = 0
        fresh = 0

        def bfs():
            while q:
                changed = False
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nrow, ncol = r + dr, c + dc
                        if (nrow in range(ROWS) and
                            ncol in range(COLS) and
                            grid[nrow][ncol] == 1):
                            q.append((nrow, ncol))
                            grid[nrow][ncol] = 2
                            changed = True
                            nonlocal fresh
                            fresh -= 1
                nonlocal time 
                if changed:
                    time += 1
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        bfs()
        if not fresh:
            return time
        else:
            return -1