# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        def invert(root):
            root.left, root.right = root.right, root.left

            if root.left and root.right:
                invert(root.left)
                invert(root.right)

            elif root.left:
                invert(root.left)
            
            elif root.right:
                invert(root.right)

            else:
                return
        
        invert(root)

        return root
