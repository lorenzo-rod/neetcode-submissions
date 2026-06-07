import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = nums[:k]
        heapq.heapify(data)
        for num in nums[k:]:
            if num > (data[0]):
                heapq.heappushpop(data, num)
        return data[0]