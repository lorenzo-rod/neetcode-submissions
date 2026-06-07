class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        maximums_l = [0] * n
        maximums_r = [0] * n
        minimums = [0] * n
        for i in range(1, n):
            maximums_l[i] = max(maximums_l[i-1], height[i-1])
            maximums_r[n-i-1] = max(maximums_r[n-i], height[n-i])
        for i in range(n):
            trapped = min(maximums_l[i], maximums_r[i]) - height[i]
            res = res + trapped if trapped > 0 else res
        return res