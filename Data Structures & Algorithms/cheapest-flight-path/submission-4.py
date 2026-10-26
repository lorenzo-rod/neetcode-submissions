import math
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [math.inf] * n
        prices[src] = 0
        tmp = prices.copy()

        for _ in range(k+1):

            for u, v, cost in flights:

                if prices[v] > tmp[u] + cost:
                    prices[v] = tmp[u] + cost
                
            tmp = prices.copy()
                
        return prices[dst] if prices[dst] != math.inf else -1
        