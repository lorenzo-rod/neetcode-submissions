from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        infinity = 2**31 - 1
        q = deque()
        m = len(grid)
        n = len(grid[0])
        directions = ((1,0), (0,1), (-1,0), (0,-1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j,0))

        while q:
            i, j, distance = q.popleft()
            for dx, dy in directions:
                n_i, n_j = i + dx, j + dy
                if -1 < n_i < m and -1 < n_j < n and grid[n_i][n_j] == infinity:
                    grid[n_i][n_j] = distance + 1
                    q.append((n_i, n_j, distance + 1))
        
        return
