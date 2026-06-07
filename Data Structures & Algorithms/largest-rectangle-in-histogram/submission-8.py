class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, height in enumerate(heights):
            index = i
            while stack and stack[-1][1] > height:
                index, bar_height = stack.pop()
                res = max(res, bar_height * (i - index))
            stack.append((index, height))
        for i, height in stack:
            res = max(res, height * (len(heights) - i))
        return res