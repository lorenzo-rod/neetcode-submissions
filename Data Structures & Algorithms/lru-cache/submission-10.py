class Node:

    def __init__(self, key = None, val = None, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.nodes = {}
        self.capacity = capacity
        self.left = Node()
        self.right = Node()

        self.left.nxt, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        node = self.nodes[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            node = Node(key, value)
            self.nodes[key] = node
            self.insert(node)

            if len(self.nodes) > self.capacity:
                key = self.left.nxt.key
                self.remove(self.left.nxt)
                del self.nodes[key]
        else:
            self.nodes[key].val = value
            self.remove(self.nodes[key])
            self.insert(self.nodes[key])

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.nxt = prev, nxt
        nxt.prev, prev.nxt = node, node

    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
        