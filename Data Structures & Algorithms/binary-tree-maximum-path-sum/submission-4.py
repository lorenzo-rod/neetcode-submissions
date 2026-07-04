# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = root.val

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal res
            res = max(res, left + node.val + right, left + node.val, right + node.val, node.val)

            return node.val + max(left, right, 0)
        
        dfs(root)
        return res