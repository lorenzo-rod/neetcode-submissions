class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        res = [[] for _ in range(len(nums) + 1)]
        output = []
        for key, value in nums_count.items():
            res[value].append(key)
        for results in reversed(res):
            for result in results:
                output.append(result)
                if len(output) == k:
                    return output