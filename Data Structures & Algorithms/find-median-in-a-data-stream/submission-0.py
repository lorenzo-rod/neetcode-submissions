import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:

        if not self.min_heap:
            self.min_heap.append(num)
            return

        if num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, - num)

        n = len(self.min_heap)
        m = len(self.max_heap)

        if n > m + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, - val)
        elif m > n + 1:
            val = - heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)


    def findMedian(self) -> float:
        n = len(self.min_heap)
        m = len(self.max_heap)

        if n > m:
            return self.min_heap[0]
        if m > n:
            return - self.max_heap[0]
            
        return (self.min_heap[0] - self.max_heap[0]) / 2
        
        