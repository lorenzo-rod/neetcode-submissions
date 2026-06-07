class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxl = height[l]
        maxr = height[r]

        res = 0

        while l <= r:
            if maxl < maxr:
                res += max(0, maxl - height[l])
                maxl = max(maxl, height[l])
                l += 1
            else:
                res += max(0, maxr - height[r])
                maxr = max(maxr, height[r])
                r -= 1
        return res