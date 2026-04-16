class CountSquares:

    def __init__(self):
        self.store = {} #(x,y): count


    def add(self, point: List[int]) -> None:
        self.store[(point[0],point[1])] = self.store.get((point[0],point[1]), 0) + 1


    def count(self, point: List[int]) -> int:
        leftDiag = []
        qx, qy = point[0], point[1]
        res = 0
        for (x,y), value in self.store.items():
            if abs(qx - x) == abs(qy - y) and qx != x:
                leftDiag.append((x,y))

        
        for (x,y) in leftDiag:
            if ((qx, y) in self.store) and ((x, qy) in self.store):
                res += self.store[(qx,y)] * self.store[(x,y)] * self.store[(x,qy)]
        
        return res
