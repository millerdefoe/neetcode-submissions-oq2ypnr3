class TicTacToe:

    def __init__(self, n: int):
        self.rows = [[0] * n for _ in range(2)]
        self.cols = [[0] * n for _ in range(2)]
        self.n = n

        #two rows to track number of moves in row for each player
        #same idea for columns
        #now we need to track the diagonals diagonal would be (0,0) - (n-1,n-1)
        self.diag = [0,0]
        #counterDiag would be (0,n) - (n,0) we find that out by x + y == n - 1
        self.counterDiag = [0,0]

        print(f"{self.counterDiag=}")

    def move(self, row: int, col: int, player: int) -> int:
        playerIndex = player - 1

        if row + col == self.n - 1:
            self.counterDiag[playerIndex] += 1
        if row == col:
            self.diag[playerIndex] += 1
        
        self.rows[playerIndex][row] += 1
        self.cols[playerIndex][col] += 1
        #print(f"{self.rows[playerIndex]=}")

        if (self.counterDiag[playerIndex] == (self.n) or
           self.diag[playerIndex] == (self.n) or 
           self.rows[playerIndex][row] == (self.n) or 
           self.cols[playerIndex][col] == (self.n)):
           return playerIndex + 1
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
