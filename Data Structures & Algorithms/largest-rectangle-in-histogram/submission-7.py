class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = heights[0]
        stack = []
        index = 0
        for i, height in enumerate(heights):
            index = i
            while (stack and stack[-1][1] > height):
                index, h = stack.pop()
                max_area = max((i - index) * h, max_area)
            stack.append((index, height))
        for i, height in stack:
            max_area = max((len(heights) - i) * height, max_area)
        return max_area