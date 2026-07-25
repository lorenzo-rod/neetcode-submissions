from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        fresh = 0
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        if fresh == 0:
            return 0
        
        while q:
            res += 1
            for _ in range(len(q)):
                i, j = q.popleft()

                for dx, dy in directions:
                    n_i, n_j = i + dx, j + dy

                    if ((-1 < n_i < len(grid))
                        and -1 < n_j < len(grid[0])
                        and grid[n_i][n_j] == 1):
                        fresh -= 1
                        grid[n_i][n_j] = 2
                        q.append((n_i, n_j))
            
            if fresh == 0:
                return res
        
        return -1