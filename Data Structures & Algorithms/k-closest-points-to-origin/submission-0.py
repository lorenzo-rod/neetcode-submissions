import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []
        for x, y in points:
            distance = x*x + y*y
            if len(self.heap) < k:
                heapq.heappush(self.heap, (-distance, x, y))
            elif distance < (-self.heap[0][0]):
                heapq.heappushpop(self.heap, (-distance, x, y))
        return [[x, y] for _, x, y in self.heap]
