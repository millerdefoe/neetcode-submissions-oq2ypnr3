class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_table: list[list[int]] = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix)+1)]
        self.m = len(matrix)
        self.n = len(matrix[0])
        self._build()

    def _build(self):
        for r in range(1, self.m + 1):
            for c in range(1, self.n + 1):
                self.prefix_table[r][c] = (
                    self.matrix[r-1][c-1]          # actual cell value
                    + self.prefix_table[r-1][c]    # row above
                    + self.prefix_table[r][c-1]    # column to the left
                    - self.prefix_table[r-1][c-1]  # remove double-counted top-left
                )

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        self._build()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix_table[row2+1][col2+1]
            - self.prefix_table[row1][col2+1]
            - self.prefix_table[row2+1][col1]
            + self.prefix_table[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
