# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        
        def dfs(root):
            left = right = 0

            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            
            if abs(left - right) > 1:
                self.is_balanced = False
             
            return 1 + max(left, right)
        
        if root:
            dfs(root)

        return self.is_balanced
            