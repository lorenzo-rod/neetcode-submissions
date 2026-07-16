class Node:

    def __init__(self, key=0, nxt=None, prv=None, val=0):
        self.key = key
        self.nxt = nxt
        self.prv = prv
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node()
        self.right = Node()
        self.left.nxt, self.right.prv = self.right, self.left
        self.nodes = {}
        

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            self.remove(node)
            self.add(node)
            node.val = value
            return
        self.nodes[key] = Node(key, None, None, value)
        self.add(self.nodes[key])
        if len(self.nodes) > self.cap:
            del self.nodes[self.left.nxt.key]
            self.remove(self.left.nxt)
    
    def remove(self, node):
        prv, nxt = node.prv, node.nxt
        prv.nxt, nxt.prv = nxt, prv
    
    def add(self, node):
        prv, nxt = self.right.prv, self.right
        prv.nxt = node
        nxt.prv = node
        node.nxt = nxt
        node.prv = prv
    
