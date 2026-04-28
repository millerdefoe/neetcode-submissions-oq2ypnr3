class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.child = None
        self.freq = 1


class LRUCache:
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.child = self.tail
        self.tail.parent = self.head
        self.size = 0


    def addMRU(self,node):
        temp = self.head.child
        self.head.child = node
        node.parent = self.head
        node.child = temp
        temp.parent = node

        self.size += 1

    def removeLRU(self)-> Node:
        temp = self.tail.parent
        self.tail.parent = self.tail.parent.parent
        self.tail.parent.child = self.tail
        
        self.size -= 1
        return temp

    def remove(self,node):
        node.parent.child = node.child
        node.child.parent = node.parent

        self.size -= 1

    def isEmpty(self)-> bool:
        if self.size:
            return False
        else:
            return True

class LFUCache:

    def __init__(self, capacity: int):
        self.LRUMap = defaultdict(LRUCache) #freq -> LRUCache
        self.nodeMap = {} #key -> Node
        self.cap = capacity #capacity
        self.min_freq = 1
        

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.LRUMap[node.freq].remove(node)
            if self.LRUMap[node.freq].isEmpty() and node.freq == self.min_freq:
                self.min_freq += 1
            node.freq += 1
            self.LRUMap[node.freq].addMRU(node)
            
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self.LRUMap[node.freq].remove(node)
            if self.LRUMap[node.freq].isEmpty() and node.freq == self.min_freq:
                self.min_freq += 1
            node.freq += 1
            self.LRUMap[node.freq].addMRU(node)
        else:
            if len(self.nodeMap) >= self.cap:
                toRemove = self.LRUMap[self.min_freq].removeLRU()
                del self.nodeMap[toRemove.key]
            node = Node(key, value)
            self.nodeMap[key] = node
            self.LRUMap[1].addMRU(node)
            self.min_freq = 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)