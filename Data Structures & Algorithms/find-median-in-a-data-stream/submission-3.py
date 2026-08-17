import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:

        if not self.min_heap or num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, - num)

        n, m = len(self.max_heap), len(self.min_heap)

        if n > m + 1:
            val = - heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif m > n + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, - val)
        

    def findMedian(self) -> float:

        n, m = len(self.max_heap), len(self.min_heap)

        if n > m:
            return - self.max_heap[0]
        elif m > n:
            return self.min_heap[0]
        
        return (self.min_heap[0] - self.max_heap[0]) / 2
        
        