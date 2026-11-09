from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = defaultdict(int)
        l = 0
        max_count = 0
        res = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            max_count = max(max_count, counter[s[r]])
            distance = r - l + 1

            if distance - max_count <= k:
                res = max(res, distance)
            else:
                counter[s[l]] -= 1
                l += 1
        
        return res
        