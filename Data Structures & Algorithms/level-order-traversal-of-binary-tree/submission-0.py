# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(root):
            if not root:
                return
            q = deque([root])
            while q:
                n_nodes = len(q)
                level_nodes = []
                for _ in range(n_nodes):
                    node = q.popleft()
                    level_nodes.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(level_nodes)
        
        bfs(root)
        return res