class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
        res = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return 0
            if j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            area = 0
            for dx, dy in directions:
                area += dfs(i + dx, j + dy)
            area += 1
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(dfs(i, j), res)
        
        return res