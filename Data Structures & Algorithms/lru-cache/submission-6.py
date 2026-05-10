class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.key_to_node = {}
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addMRU(self, head, node):
        temp = head.next
        head.next = node
        node.next = temp
        node.prev = head
        temp.prev = node

    def removeLRU(self, tail)->Node:
        temp = tail.prev
        tail.prev = tail.prev.prev
        tail.prev.next = tail
        return temp


    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        else:
            node = self.key_to_node[key]
            self.removeNode(node)
            self.addMRU(self.head, node)
            return node.value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node:
            node = Node(key, value)
            if len(self.key_to_node) == self.capacity:
                temp = self.removeLRU(self.tail)
                self.addMRU(self.head, node)
                del self.key_to_node[temp.key]
            else:
                self.addMRU(self.head, node)
            self.key_to_node[key] = node
        else:
            node = self.key_to_node[key]
            self.removeNode(node)
            self.addMRU(self.head, node)
            node.value = value


        
