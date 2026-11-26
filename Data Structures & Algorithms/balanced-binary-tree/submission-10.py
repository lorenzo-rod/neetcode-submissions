# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        res = True

        def dfs(node):

            nonlocal res
            if not node or not res:
                return 0

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)

            if res:
                res = abs(left - right) < 2
            
            return max(left, right)
        
        dfs(root)

        return res
        