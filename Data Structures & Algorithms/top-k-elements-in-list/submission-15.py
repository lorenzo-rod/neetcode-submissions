class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in  range(len(nums))]
        nums_counter = Counter(nums)
        res = [0] * k

        for key, value in nums_counter.items():
            bucket[value-1].append(key)
        
        count = 0
        for numbers in reversed(bucket):
            for num in numbers:
                res[count] = num
                count += 1
                if count == k:
                    return res
        