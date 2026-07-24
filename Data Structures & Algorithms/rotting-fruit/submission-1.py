from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        res = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: 
                    q.append((i, j))

        while q:
            res += 1
            for _ in range(len(q)):
                i, j = q.popleft()

                for dx, dy in directions:
                    n_i, n_j = i + dx, j + dy
                    if ((-1 < n_i < len(grid)) 
                        and (-1 < n_j < len(grid[0]))
                        and (grid[n_i][n_j] == 1)):
                        grid[n_i][n_j] = 2
                        q.append((n_i, n_j))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return res - 1 if res != 0 else res


        



































