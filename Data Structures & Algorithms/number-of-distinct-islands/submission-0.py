class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        shapes = set() #size: order

        visited = set()
        distinct = 0

        def dfs(i, j, came_from, path):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            
            if grid[i][j] == 0:
                return
            if (i,j) in visited:
                return
            visited.add((i,j))
            path.append(came_from)  
            dfs(i+1, j, 1, path)
            dfs(i-1, j, 2, path)
            dfs(i, j+1, 3, path)
            dfs(i, j-1, 4, path)
            path.append(0) 
            
            return path
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    path = []
                    dfs(i, j, 0, path)
                    shapes.add(tuple(path))  # set handles duplicates automatically

        return len(shapes)

