from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        char_count = defaultdict(int)
        max_count = 0

        for r in range(len(s)):
            char_count[s[r]] += 1
            max_count = max(char_count.values())
            distance = r - l + 1

            if distance - max_count <= k:
                res = max(res, distance)
            else:
                char_count[s[l]] -= 1
                l += 1
        
        return res