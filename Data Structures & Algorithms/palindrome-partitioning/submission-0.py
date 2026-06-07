class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def isPali(l, r):
            while(l < r):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(path, idx):
            if idx == len(s):
                res.append(path[:])
                return
            for i in range(idx, len(s)):
                if isPali(idx, i):
                    path.append(s[idx:i+1])
                    backtrack(path, i + 1)
                    path.pop()
        
        backtrack([], 0)

        return res
