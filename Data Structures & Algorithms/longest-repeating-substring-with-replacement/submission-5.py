from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            char_count[s[r]] += 1
            max_count = max(char_count.values())

            if r - l + 1 - max_count <= k:
                res = max(res, r - l + 1)
            else:
                char_count[s[l]] -= 1
                l += 1
        
        return res