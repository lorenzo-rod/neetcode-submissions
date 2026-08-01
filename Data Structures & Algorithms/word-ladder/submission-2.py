from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        neighbors = defaultdict(list)
        wordList.append(beginWord)
        m = len(beginWord)

        for word in wordList:
            for i in range(m):
                pattern = word[0:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set()

        while q:
            word, count = q.popleft()
            if word == endWord:
                return count

            visited.add(word)
            
            for i in range(m):
                pattern = word[0:i] + "*" + word[i+1:]
                for nei in neighbors[pattern]:
                    if nei not in visited:
                        q.append((nei, count + 1))
        
        return 0
            