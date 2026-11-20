from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []

        for num, freq in counter.items():
            bucket[freq].append(num)
        
        for numbers in reversed(bucket):
            for num in numbers:
                res.append(num)
                if len(res) == k:
                    return res
                    