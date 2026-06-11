from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        res = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.discard(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        
        return res
                
