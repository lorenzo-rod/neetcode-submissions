import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = - heapq.heappop(stones)
            y = - heapq.heappop(stones)

            if x == y:
                continue
            elif x > y:
                res = x - y
            else:
                res = y - x
            
            heapq.heappush(stones, - res)
        
        return - stones[0] if stones else 0
