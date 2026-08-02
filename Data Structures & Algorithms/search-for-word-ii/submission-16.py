class Node:

    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def add_word(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = Node()
        res = []
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        for word in words:
            root.add_word(word)
        
        visited = set()
        
        def dfs(node, word, i, j):
            if not (-1 < i < len(board)):
                return
            if not (-1 < j < len(board[0])):
                return
            if (i, j) in visited:
                return
            if board[i][j] not in node.children:
                return

            c = board[i][j]
            word += c
            node = node.children[c]

            if node.is_end:
                res.append(word)
                node.is_end = False
            
            visited.add((i, j))
            for dx, dy in directions:
                dfs(node, word, i + dx, j + dy)
            visited.remove((i, j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(root, "", i, j)

        return res

