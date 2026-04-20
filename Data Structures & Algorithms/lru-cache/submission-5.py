class Node:
    def __init__(self, key, value):
        self.parent = None
        self.child = None
        self.key = key 
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.hMap = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.child = self.tail
        self.tail.parent = self.head
        self.capacity = capacity

    def insertBeforeTail(self, node):
        self.tail.parent.child = node
        node.child = self.tail
        node.parent = self.tail.parent
        self.tail.parent = node


        

    def get(self, key: int) -> int:
        if key in self.hMap:
            #need to update this to most recent
            target = self.hMap[key]
            target.parent.child = target.child
            target.child.parent = target.parent
            self.insertBeforeTail(target)
            return self.hMap[key].value
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.hMap:
            target = self.hMap[key]
            target.parent.child = target.child
            target.child.parent = target.parent
            self.insertBeforeTail(target)
            self.hMap[key].value = value
        else:
            if len(self.hMap) >= self.capacity:
                temp = self.head.child
                del self.hMap[temp.key]
                self.head.child = temp.child
                temp.child.parent = self.head

            newNode = Node(key, value)
            self.insertBeforeTail(newNode)
            self.hMap[key] = newNode

                
