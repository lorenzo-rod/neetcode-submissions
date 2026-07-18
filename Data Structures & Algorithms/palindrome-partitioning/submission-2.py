class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(substrings, idx):
            if idx == len(s):
                res.append(substrings[:])
                return
            for i in range(idx, len(s)):
                if isPali(idx, i):
                    substrings.append(s[idx:i+1])
                    backtrack(substrings, i + 1)
                    substrings.pop()
        
        backtrack([], 0)
        return res
        
        