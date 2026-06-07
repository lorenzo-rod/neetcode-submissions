from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
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
            if items:
                for item in items:
                    res.append(item)
                if len(res) >= k:
                    return res[-k:]
        