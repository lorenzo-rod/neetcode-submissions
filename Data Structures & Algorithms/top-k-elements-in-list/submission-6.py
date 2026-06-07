class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        res = [0] * k
        i = 0
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in nums_counter.items():
            buckets[value].append(key)
        for bucket in reversed(buckets):
            for number in bucket:
                res[i] = number
                i += 1
                if i == k:
                    return res