class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zeroPos = set()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeroPos.add((r,c))

        for zero in zeroPos:
            for r in range(ROWS):
                matrix[r][zero[1]] = 0
            for c in range(COLS):
                matrix[zero[0]][c] = 0


                
        