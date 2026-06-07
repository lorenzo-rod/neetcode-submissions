class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        start_numbers = []
        for num in nums:
            if num - 1 not in nums:
                start_numbers.append(num)
        max_len = 0
        for start_number in start_numbers:
            curr_len = 0
            number = start_number
            while(number in nums_set):
                curr_len += 1
                number += 1
            max_len = max(max_len, curr_len)
        return max_len