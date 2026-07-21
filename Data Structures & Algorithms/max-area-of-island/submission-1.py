class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
        area = 0
        res = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == 0:
                return
            
            nonlocal area
            area += 1

            grid[i][j] = 0
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    res = max(area, res)
        
        return res