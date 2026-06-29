# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        q = deque([(root, -101)])
        res = 0

        while q:
            node, maximum = q.popleft()

            if node.val >= maximum:
                res += 1
            
            if node.left:
                q.append((node.left, max(node.val, maximum)))
            
            if node.right:
                q.append((node.right, max(node.val, maximum)))
            
        return res