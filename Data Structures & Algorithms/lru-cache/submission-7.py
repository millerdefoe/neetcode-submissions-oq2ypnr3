class Node:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.value = value
        self.parent = None
        self.child = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.child = self.tail
        self.tail.parent = self.head
        self.key_to_node = {}
        self.capacity = capacity

    def addMRU(self, head, node):
        temp = head.child
        head.child = node
        temp.parent = node
        node.child = temp
        node.parent = head

    def remove(self, node):
        node.parent.child = node.child
        node.child.parent = node.parent

    def removeLRU(self, tail):
        temp = tail.parent
        self.remove(temp)
        return temp

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)
            self.addMRU(self.head, node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)
            self.addMRU(self.head, node)
            node.value = value
        else:
            if len(self.key_to_node) == self.capacity:
                lru_node = self.removeLRU(self.tail)
                del self.key_to_node[lru_node.key]
            
            node = Node(key, value)
            self.key_to_node[key] = node
            self.addMRU(self.head, node)