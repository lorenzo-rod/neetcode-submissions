class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {len(s) : True}

        
        def add(i):
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                for c in word:
                    if (((i + len(word)) <= len(s)) 
                       and (s[i:i + len(word)] == word)):
                       if add(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return add(0)
