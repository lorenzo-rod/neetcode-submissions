import math
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        res = [0] * k
        for i in range(k):
            max_key = 0
            max_value = -math.inf
            for key, value in nums_counter.items():
                if value > max_value:
                    max_value = value
                    max_key = key
            res[i] = max_key
            del nums_counter[max_key]
        return res