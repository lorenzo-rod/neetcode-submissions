class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        visited = set()

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(i, j, ocean):
            visited.add((i, j))
            ocean.add((i, j))

            for dx, dy in directions:
                n_i, n_j = i + dx, j + dy
                if ((-1 < n_i < len(heights)) 
                    and (-1 < n_j < len(heights[0]))
                    and ((heights[i][j] <= heights[n_i][n_j]))
                    and (n_i, n_j) not in visited):
                    dfs(n_i, n_j, ocean)

        for i in range(len(heights)):
            dfs(i, 0, pacific)
            visited.clear()

        for j in range(len(heights[0])):
            dfs(0, j, pacific)
            visited.clear()
        
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, atlantic)
            visited.clear()
        
        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, atlantic)
            visited.clear()

        return list(pacific & atlantic)
