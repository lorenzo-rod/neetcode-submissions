import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        n = len(grid)

        heap = [(0, 0, 0)]
        explored = set()
        maximum = grid[0][0]

        while (n-1, n-1) not in explored:
            h, nx, ny = heapq.heappop(heap)

            if (nx, ny) in explored:
                continue
            
            explored.add((nx, ny))
            maximum = max(maximum, h)

            for dx, dy in directions:
                neix, neiy = nx + dx, ny + dy

                if not -1 < neix < n:
                    continue
                
                if not -1 < neiy < n:
                    continue
                
                if (neix, neiy) not in explored:
                    heapq.heappush(heap, (grid[neix][neiy], neix, neiy))
        
        return maximum
