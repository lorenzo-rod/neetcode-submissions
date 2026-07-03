class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        chars = set()
        res = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.discard(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, len(chars))
        
        return res