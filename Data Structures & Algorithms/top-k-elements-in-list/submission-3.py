import math
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        nums_freq = [[] for _ in range(len(nums) + 1)]
        for key, value in nums_counter.items():
            nums_freq[value].append(key)
        res = []
        for numbers in reversed(nums_freq):
            for number in numbers:
                res.append(number)
            if len(res) == k:
                break
        return res