class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        res = 0

        for num in nums:
            start = num
            while start - 1 in nums_set:
                start -= 1
            number = start
            count = 0
            while number in nums_set:
                nums_set.discard(number)
                count += 1
                number += 1
                res = max(res, count)
        
        return res
