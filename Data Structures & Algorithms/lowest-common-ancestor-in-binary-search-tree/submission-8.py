# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        node = root

        while node:

            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                return node
            elif node.val <= p.val and node.val <= q.val:
                node = node.right
            else:
                node = node.left
        