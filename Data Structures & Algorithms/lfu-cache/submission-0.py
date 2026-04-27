class Node:
    
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.use = 1
        self.parent = None
        self.child = None

class LRUCache:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.child = self.tail
        self.tail.parent = self.head
        self.size = 0

    def add_mru(self, node):
        temp = self.head.child    
        self.head.child = node
        node.parent = self.head
        node.child = temp
        temp.parent = node
        self.size += 1

    def remove_lru(self):  
        lru = self.tail.parent          # save it before unlinking
        self.tail.parent.parent.child = self.tail
        self.tail.parent = lru.parent
        self.size -= 1
        return lru  
        
    
    def remove(self, node):
        temp = node.child
        node.child.parent = node.parent
        node.parent.child = temp
        self.size -= 1

    def is_empty(self): 
        return not self.size
    
class LFUCache:

    def __init__(self, capacity: int):
        self.freq_list = defaultdict(LRUCache)
        self.key_to_node = {}
        self.cap = capacity  
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.freq_list[node.use].remove(node)
            if self.freq_list[node.use].is_empty() and node.use == self.min_freq:
                self.min_freq += 1
            node.use += 1
            self.freq_list[node.use].add_mru(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.freq_list[node.use].remove(node)
            if self.freq_list[node.use].is_empty() and node.use == self.min_freq:
                self.min_freq += 1
            node.use += 1
            self.freq_list[node.use].add_mru(node)
        else:
            if len(self.key_to_node) < self.cap:
                node = Node(key, value)
                self.key_to_node[key] = node
                self.freq_list[node.use].add_mru(node)
                self.min_freq = 1
            else:
                toRemove = self.freq_list[self.min_freq].remove_lru()
                del self.key_to_node[toRemove.key]
                node = Node(key, value)
                self.key_to_node[key] = node
                self.freq_list[node.use].add_mru(node)
                self.min_freq = 1


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)