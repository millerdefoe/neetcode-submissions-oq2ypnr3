class TicTacToe:

    def __init__(self, n: int):
        self.rows = [[0 for _ in range(n)] for _ in range(2)]
        self.cols = [[0 for _ in range(n)] for _ in range(2)]
        self.diagonals = [[0 for _ in range(2)] for _ in range(2)]
        self.n = n


    def move(self, row: int, col: int, player: int) -> int:
        p = player - 1  # 0 for player 1, 1 for player 2
        self.rows[p][row] += 1
        self.cols[p][col] += 1
        if row == col:
            self.diagonals[p][0] += 1
        if row + col == self.n - 1:
            self.diagonals[p][1] += 1

        if (self.rows[p][row] == self.n or
            self.cols[p][col] == self.n or
            self.diagonals[p][0] == self.n or
            self.diagonals[p][1] == self.n):
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
