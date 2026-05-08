class Excel:

    def __init__(self, height: int, width: str):
        self.formula = {}
        self.sheet = [[0] * (ord(width) - ord('A') + 1) for _ in range(height)]
        

    def set(self, row: int, column: str, val: int) -> None:
        self.sheet[row - 1][ord(column) - ord('A')] = val
        if (row, column) in self.formula:
            del self.formula[(row, column)]

    def get(self, row: int, column: str) -> int:
        res = 0

        if (row, column) not in self.formula:
            return self.sheet[row - 1][ord(column) - ord('A')]
        
        for pos in self.formula[(row, column)]:
            res += self.get(int(pos[1:]), pos[0])
        
        return res

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cells = []
        for number in numbers:
            if ":" not in number:
                cells.append(number)
            else:
                start, end = number.split(":")
                for i in range(int(start[1:]), int(end[1:]) + 1):
                    for j in range(ord(start[0]), ord(end[0]) + 1):
                        cells.append(chr(j) + str(i))
        
        self.formula[(row, column)] = cells[:]

        return self.get(row, column)

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
