class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if (x,y) == (0,0):
            return 0
        
        x, y = abs(x), abs(y)
        
        directions = {(2,1), 
                      (2,-1), 
                      (-2,1), 
                      (-2,-1), 
                      (1,2), 
                      (-1,2), 
                      (1,-2),
                      (-1,-2)}
        
        #parent = {(0,0): None}
        q = deque()
        steps = 0
        q.append((0,0))
        target = (x,y)
        visited = {(0,0)}
        while q:
            
            for _ in range(len(q)):
                pos = q.popleft()

                if pos == target:
                    return steps


                for d in directions:
                    new_pos = (pos[0]+d[0], pos[1]+d[1])
                    if new_pos not in visited and new_pos[0] >= -2 and new_pos[1] >= -2:
                        visited.add(new_pos)
                        q.append(new_pos)
            steps += 1


        