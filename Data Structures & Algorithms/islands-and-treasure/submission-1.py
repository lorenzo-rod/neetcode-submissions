from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m = len(grid)
        n = len(grid[0])

        def bfs(i, j):
            q = deque([(i, j, 0)])
            explored = set((i, j))
            while q:
                i, j, distance = q.popleft()
                for dx, dy in directions:
                    n_i, n_j = i + dx, j + dy
                    if (
                        -1 < n_i < m
                        and -1 < n_j < n
                        and grid[n_i][n_j] > 0
                        and (n_i, n_j) not in explored
                    ):
                        explored.add((n_i, n_j))
                        q.append((n_i, n_j, distance + 1))
                        if grid[n_i][n_j] > distance + 1:
                            grid[n_i][n_j] = distance + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i, j)
