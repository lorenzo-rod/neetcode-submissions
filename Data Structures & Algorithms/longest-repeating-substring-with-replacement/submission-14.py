from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = defaultdict(int)
        res = 0

        l = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            max_count = max(counter.values())
            distance = r - l + 1

            if distance - max_count > k:
                counter[s[l]] -= 1
                l += 1
                distance = r - l + 1
                max_count = max(counter.values())

            res = max(res, distance)

        return res
