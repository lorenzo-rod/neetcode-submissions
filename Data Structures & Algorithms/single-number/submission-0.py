class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]

        for num in nums[1:len(nums)]:
            res = res ^ num
        
        return res