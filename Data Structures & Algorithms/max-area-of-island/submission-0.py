class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            stack = [(i, j)]
            area = 0
            grid[i][j] = -1
            while stack:
                i, j = stack.pop()
                area += 1
                for dx, dy in directions:
                    n_i, n_j = i + dx, j + dy
                    if (-1 < n_i < m and -1 < n_j < n) and grid[n_i][n_j] == 1:
                        stack.append((n_i, n_j))
                        grid[n_i][n_j] = -1
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))

        return max_area
