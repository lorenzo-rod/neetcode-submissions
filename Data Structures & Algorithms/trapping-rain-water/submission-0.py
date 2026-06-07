class Solution:
    def trap(self, height: List[int]) -> int:
        left_heights = [0] * len(height)
        right_heights = [0] * len(height)
        trapped_waters = [0] * len(height)
        for i in range(1, len(height)):
            left_heights[i] = max(left_heights[i-1], height[i-1])
        for i in reversed(range(len(height) - 1)):
            right_heights[i] = max(right_heights[i+1], height[i+1])
        for i in range(1, len(height) - 1):
            trapped_waters[i] = max(min(left_heights[i], right_heights[i]) - height[i], 0)
        return sum(trapped_waters)