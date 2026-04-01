class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9, 9
        rowhash = defaultdict(set)
        colhash = defaultdict(set)
        boxhash = defaultdict(set)

        for row in range(ROWS):
            
            for col in range(COLS):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rowhash[row] or board[row][col] in colhash[col] or board[row][col] in boxhash[(row//3, col//3)]):
                    return False
                colhash[col].add(board[row][col])
                rowhash[row].add(board[row][col])
                boxhash[row//3,col//3].add(board[row][col])
                

        return True