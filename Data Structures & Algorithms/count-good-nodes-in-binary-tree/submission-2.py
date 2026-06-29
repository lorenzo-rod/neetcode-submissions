# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        q = deque([(root, root.val)])
        res = 1

        while q:
            node, maximum = q.popleft()

            if node.left:
                if node.left.val >= maximum:
                    res += 1
                    q.append((node.left, node.left.val))
                else:
                    q.append((node.left, maximum))
            
            if node.right:
                if node.right.val >= maximum:
                    res += 1
                    q.append((node.right, node.right.val))
                else:
                    q.append((node.right, maximum))
        
        return res