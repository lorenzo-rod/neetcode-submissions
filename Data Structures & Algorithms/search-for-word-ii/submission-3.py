class Node:

    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def addWord(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_end = True
        


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j, node, word):
            if i < 0 or i >= len(board):
                return
            if j < 0 or j >= len(board[0]):
                return
            if board[i][j] not in node.children:
                return

            word += board[i][j]
            node = node.children[board[i][j]]
            if node.is_end:
                res.add(word)
            tmp, board[i][j] = board[i][j], "#"
            for dx, dy in directions:
                dfs(i + dx, j + dy, node, word)
            board[i][j] = tmp
        
        trie = Node()

        for word in words:
            trie.addWord(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie, "")
            
        return list(res)

            
