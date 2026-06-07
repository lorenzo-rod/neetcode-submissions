class Node:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.nxt, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.nxt = prev, nxt
        prev.nxt, nxt.prev = node, node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) == self.cap:
                lru = self.left.nxt
                self.remove(lru)
                del self.cache[lru.key]
            self.cache[key] = Node(key,value)
            self.insert(self.cache[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)