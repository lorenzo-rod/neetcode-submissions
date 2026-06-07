class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in nums_set:
                curr_len = 0
                while(num in nums_set):
                    curr_len += 1
                    num += 1
                max_len = max(max_len, curr_len)
        return max_len