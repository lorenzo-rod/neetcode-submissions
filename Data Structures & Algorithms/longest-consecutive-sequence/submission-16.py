class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        res = 0

        for num in nums:
            if num in nums_set:
                count = 0
                start = num
                while start - 1 in nums_set:
                    start -= 1
                
                num = start
                while num in nums_set:
                    nums_set.remove(num)
                    count += 1
                    num += 1
                res = max(res, count)

        return res
