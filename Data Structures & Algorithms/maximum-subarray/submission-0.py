class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        curr_sum = - float("inf")
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            maximum = max(maximum, curr_sum)
        return maximum