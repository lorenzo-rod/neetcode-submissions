class Node:

    def __init__(self, val, key, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.node_map = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next, self.right.prev = self.right, self.left

    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return - 1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self._remove(node)
            self._insert(node)
        else:
            self.node_map[key] = node = Node(value, key)
            self._insert(node)

            if len(self.node_map) > self.cap:
                del self.node_map[self.left.next.key]
                self._remove(self.left.next)






