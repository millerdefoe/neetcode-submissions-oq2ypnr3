class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #djikstras since its a path and not a spanning tree? Else we would use Prim's
        minHeap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        ROWS, COLS = len(grid), len(grid[0])

        while minHeap:
            dist, r, c = heapq.heappop(minHeap)
            visited.add((r,c))

            if (r == ROWS - 1 and c == COLS - 1):
                return dist
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # The cost to reach a cell is the max of current path cost and new cell elevation
                    heapq.heappush(minHeap, (max(dist, grid[nr][nc]), nr, nc))
                
        return -1
        