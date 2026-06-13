from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) + 1
        buckets = [[] for _ in range(n)]
        nums_counter = defaultdict(int)
        res = []

        for num in nums:
            nums_counter[num] += 1
        
        for value, freq in nums_counter.items():
            buckets[freq].append(value)

        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res