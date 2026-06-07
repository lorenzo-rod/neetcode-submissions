class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sequence = 0
        res = 0

        for num in nums:
            if num - 1 not in nums_set:
                while num in nums_set:
                    sequence += 1
                    num += 1
                res = max(res, sequence)
                sequence = 0
        
        return res
            
        

        