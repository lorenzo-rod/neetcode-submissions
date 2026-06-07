import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = []
        for num in nums:
            if len(data) < k:
                heapq.heappush(data, num)
            elif num > (data[0]):
                heapq.heappushpop(data, num)
        return data[0]