class Excel:

    def __init__(self, height: int, width: str):
        self.sheet = [[0] * (ord(width) - ord('A') + 1) for _ in range(height)]
        self.formula = {}

    def set(self, row: int, column: str, val: int) -> None:
        self.sheet[row - 1][ord(column) - ord('A')] = val
        if (row, column) in self.formula:
            del self.formula[(row,column)]

    def get(self, row: int, column: str) -> int:
        if (row, column) in self.formula:
            total = 0
            for cell in self.formula[(row,column)]:
                total += self.get(int(cell[1:]), cell[0])
            return total
        else:
            return self.sheet[row - 1][ord(column) - ord('A')]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cells = []
        for number in numbers:
            if ":" not in number:
                cells.append(number)
            else:
                sep = number.split(":")
                for i in range(int(sep[0][1:]), int(sep[1][1:]) + 1):
                    for j in range(ord(sep[0][0]) - ord('A'), ord(sep[1][0]) - ord('A') + 1):
                        val = chr(j + ord('A')) + str(i)
                        cells.append(val)
        
        self.formula[(row,column)] = cells
        return self.get(row, column)


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)

