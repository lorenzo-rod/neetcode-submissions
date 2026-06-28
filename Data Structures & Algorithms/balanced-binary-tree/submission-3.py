# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node):
            
            left = right = 0

            if node.left:
                left = dfs(node.left)
                if left == - 1:
                    return - 1
            if node.right:
                right = dfs(node.right)
                if right == - 1:
                    return -1
            
            if abs(left - right) > 1:
                return - 1
            
            return 1 + max(left, right)
        
        return dfs(root) != -1