class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        maxl = height[0]
        maxr = height[n-1]

        l, r = 1, n - 2

        res = 0

        while l <= r:

            if maxl < maxr:
                res += max(0, maxl - height[l])
                maxl = max(height[l], maxl)
                l += 1
            else:
                res += max(0, maxr - height[r])
                maxr = max(height[r], maxr)
                r -= 1

        return res
