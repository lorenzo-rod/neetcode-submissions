class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        count_map = Counter(nums)
        buckets = [[] for _ in  range(len(nums) + 1)]
        for key, value in count_map.items():
            buckets[value].append(key)
        i = 0
        for bucket in reversed(buckets):
            for num in bucket:
                res[i] = num
                i += 1
                if i == k:
                    return res