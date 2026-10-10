from collections import defaultdict
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(grid)

        nodes = {}
        heap = [(grid[0][0], 0, 0)]
        maximum = 0

        while (n - 1, n - 1) not in nodes:
            w1, ni, nj = heapq.heappop(heap)

            if (ni, nj) in nodes:
                continue

            nodes[(ni, nj)] = w1
            maximum = max(w1, maximum)

            for dx, dy in directions:
                ni2, nj2 = ni + dx, nj + dy

                if not(-1 < ni2 < n):
                    continue

                if not(-1 < nj2 < n):
                    continue

                if (ni2, nj2) not in nodes:
                    heapq.heappush(heap, (grid[ni2][nj2], ni2, nj2))

        return maximum       
