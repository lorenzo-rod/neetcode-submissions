# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        q = deque([root])
        res = 1

        while q:
            node = q.pop()

            if node.left:
                if node.left.val >= node.val:
                    res += 1
                else:
                    node.left.val = node.val
                q.append(node.left)
            
            if node.right:
                if node.right.val >= node.val:
                    res += 1
                else:
                    node.right.val = node.val
                q.append(node.right)
        
        return res
        

