# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val : i for i, val in enumerate(inorder)}
        self.root_idx = 0

        def build(left, right):
            if left > right:
                return None
            val = preorder[self.root_idx]
            self.root_idx += 1
            root = TreeNode(val)
            i = inorder_idx[val]
            root.left = build(left, i - 1)
            root.right = build(i + 1, right)
            return root
        
        root = build(0, len(preorder) - 1)
        return root
