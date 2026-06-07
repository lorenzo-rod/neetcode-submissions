class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)

        if len(nums_set) == 1:
            return 1

        sequence = 0
        res = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                while num in nums_set:
                    sequence += 1
                    num += 1
                res = max(res, sequence)
                sequence = 0
        
        return res
            
        

        