from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v,w))
        
        q = deque([(0, 0, src)])
        prices = [float("inf")] * n
        prices[src] = 0

        while q:
            price, stops, node = q.popleft()
            if stops > k:
                continue

            for neighbor, cost in graph[node]:
                new_cost = price + cost
                if new_cost < prices[neighbor]:
                    prices[neighbor] = new_cost
                    q.append((new_cost, stops + 1, neighbor))

        return prices[dst] if prices[dst] != float("inf") else -1