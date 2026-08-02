class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        memo = [False] * (n + 1)
        memo[n] = True

        for i in reversed(range(n)):
            for word in wordDict:
                for c in word:
                    if (((i + len(word)) <= len(s)) 
                       and (s[i:i + len(word)] == word)):
                       if memo[i + len(word)]:
                        memo[i] = True

        return memo[0]
