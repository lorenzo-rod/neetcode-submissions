# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minimum = - math.inf
        maximum = math.inf

        def dfs(node, minimum, maximum):
            if not node:
                return True
            if node.val <= minimum:
                return False
            if node.val >= maximum:
                return False
            
            return dfs(node.left, minimum, node.val) and dfs(node.right, node.val, maximum)
        
        return dfs(root, minimum, maximum)
