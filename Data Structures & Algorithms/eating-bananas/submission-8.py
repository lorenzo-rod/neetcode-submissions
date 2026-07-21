import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = max((sum(piles)) // h, 1)
        r = max(piles)
        res = l

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += int(math.ceil(pile / m))
            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res