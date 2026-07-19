import math
class Node:

    def __init__(self):
        self.children = {}
        self.is_end = False
        self.refs = math.inf
    
    def addWord(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            node.refs += 1
        node.is_end = True
    
    def removeWord(self, word):
        node = self
        for c in word:
            prev = node
            node = node.children[c]
            node.refs -= 1
            if node.refs == 0:
                del prev.children[c]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        trie = Node()

        for word in words:
            trie.addWord(word)

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
                trie.removeWord(word)

            tmp, board[i][j] = board[i][j], "."

            for dx, dy in directions:
                dfs(i + dx, j + dy, node, word)
            
            board[i][j] = tmp
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie, "")
                
        return list(res)
        
