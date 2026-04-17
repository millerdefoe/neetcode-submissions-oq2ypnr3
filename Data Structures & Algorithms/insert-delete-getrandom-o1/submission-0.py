class RandomizedSet:

    def __init__(self):
        self.store = set()

    def insert(self, val: int) -> bool:
        self.store.add(val)
        return val in self.store

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False
        self.store.remove(val)
        return True


    def getRandom(self) -> int:
        num = self.store.pop()
        self.store.add(num)
        return num
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()