class Node:

    def __init__(self, key = None, value = None, prev = None, nxt = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.left = Node()
        self.right = Node()
        self.left.nxt = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            self.remove(node)
            self.insert(node)
            node.value = value
        else:
            if len(self.nodes) == self.capacity:
                del self.nodes[self.left.nxt.key]
                self.remove(self.left.nxt)
                node = Node(key, value)
                self.insert(node)
                self.nodes[key] = node
            else:
                node = Node(key, value)
                self.insert(node)
                self.nodes[key] = node
            
    
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
        node.prev, node.nxt = None, None

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.nxt = prev, nxt
        prev.nxt, nxt.prev = node, node

