class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        stack = []

        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, height * (i - index))
            stack.append((index, h))
            
        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
            
        return res
