class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        i = 0
        res = [0] * k
        bucket = [[] for _ in range(len(nums) + 1)]
        count_map = {}
        for num in nums:
            if num not in count_map:
                count_map[num] = 1
            else:
                count_map[num] += 1
        for key, value in count_map.items():
            bucket[value].append(key)
        for items in reversed(bucket):
            for item in items:
                res[i] = item
                i += 1
                if i == k:
                    return res
        