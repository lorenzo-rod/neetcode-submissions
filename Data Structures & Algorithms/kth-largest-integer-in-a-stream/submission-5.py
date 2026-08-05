import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = nums
        self.k = k
        heapq.heapify(self.data)
        while len(self.data) > k:
            heapq.heappop(self.data)

    def add(self, val: int) -> int:
        if len(self.data) < self.k:
            heapq.heappush(self.data, val)
            return self.data[0]
        if val < self.data[0]:
            return self.data[0]
        else:
            heapq.heappushpop(self.data, val)
            return self.data[0]
