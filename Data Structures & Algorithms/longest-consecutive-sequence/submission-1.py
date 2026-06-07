class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        minimum = min(nums)
        maximum = max(nums)
        nums_set = set(nums)
        max_len = 0
        curr_len = 0
        num = minimum
        while(num <= maximum):
            if num in nums_set:
                curr_len += 1
                num += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 0
                num += 1
        max_len = max(max_len, curr_len)
        return max_len