from collections import deque

class Node:

    def __init__(self, word):
        self.word = word
        self.neighbors = set()

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        m = len(beginWord)
        begin_node = Node(beginWord)
        nodes = [begin_node] + [Node(word) for word in wordList]

        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                matches = 0
                for k in range(m):
                    if nodes[i].word[k] == nodes[j].word[k]:
                        matches += 1
                if matches == m - 1:
                    nodes[i].neighbors.add(nodes[j])
                    nodes[j].neighbors.add(nodes[i])
        
        q = deque([(begin_node, 1)])
        visited = set()

        while q:
            node, count = q.popleft()
            if node.word == endWord:
                return count

            visited.add(node)
            
            for nei in node.neighbors:
                if nei not in visited:
                    q.append((nei, count + 1))

        return 0
