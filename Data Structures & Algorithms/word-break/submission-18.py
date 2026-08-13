class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [False] * (n+1)
        memo[n] = True

        for i in reversed(range(n)):
            for word in wordDict:
                if i + len(word) <= n:
                    if s[i:i+len(word)] == word and memo[i+len(word)]:
                        memo[i] = True
            
        return memo[0]
