"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        node_map = {}
        node = head
        while(node):
            node_map[node] = Node(node.val, None, None)
            node = node.next
        for key_node, value_node in node_map.items():
            value_node.next = node_map[key_node.next] if key_node.next else None
            value_node.random = node_map[key_node.random] if key_node.random else None
        return node_map[head]