from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList.append(beginWord)
        visited = set()
        m = len(beginWord)

        neighbors = defaultdict(list)

        for word in wordList:
            for i in range(m):
                key = word[0:i] + "*" + word[i+1:]
                neighbors[key].append(word)
        
        q = deque([(beginWord, 1)])

        while q:
            word, count = q.popleft()

            visited.add(word)
            for i in range(m):
                key = word[0:i] + "*" + word[i+1:]
                for nei in neighbors[key]:
                    if nei not in visited:
                        if nei == endWord:
                            return count + 1
                        q.append((nei, count + 1))
        
        return 0