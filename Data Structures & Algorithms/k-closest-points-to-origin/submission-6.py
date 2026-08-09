import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for i in range(k):
            distance = points[i][0]**2 + points[i][1]**2
            heapq.heappush(heap, (-distance, points[i]))

        for i in range(k, len(points)):
            distance = points[i][0]**2 + points[i][1]**2
            print(distance, heap[0][0])
            print(points[i])
            if distance < -heap[0][0]:
                heapq.heappushpop(heap, (-distance, points[i]))
        print(heap)
        return [point for _, point in heap]
