import math
class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        stack = []
        maximum = - math.inf

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            
            if num > maximum:
                stack.append(num)
            
            maximum = max(maximum, num)

        return len(stack)

            
        