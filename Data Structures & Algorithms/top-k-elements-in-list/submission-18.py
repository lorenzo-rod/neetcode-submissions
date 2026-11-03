class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        counter = Counter(nums)

        res = []

        for key, value in counter.items():
            buckets[value].append(key)

        while True:
            for numbers in reversed(buckets):
                for num in numbers:
                    res.append(num)
                    if len(res) == k:
                        return res

