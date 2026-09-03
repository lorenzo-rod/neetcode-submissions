from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()

        m = len(grid)
        n = len(grid[0])

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            i, j, distance = q.popleft()

            for dx, dy in directions:
                n_i, n_j = i + dx, j + dy

                if not(-1 < n_i < m):
                    continue
                
                if not(-1 < n_j < n):
                    continue

                if grid[n_i][n_j] == INF:
                    grid[n_i][n_j] = grid[i][j] + 1
                    q.append((n_i, n_j, distance + 1))

