# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = { val : i for i, val in enumerate(inorder)}
        self.root_idx = 0

        def build(left, right):
            if left > right:
                return None
            root = TreeNode(preorder[self.root_idx])
            self.root_idx += 1
            m = inorder_idx[root.val]
            root.left = build(left, m - 1)
            root.right = build(m + 1, right)
            return root
        
        return build(0, len(preorder) - 1)