class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(i, j, ocean):
            ocean.add((i, j))

            for dx, dy in directions:
                n_i, n_j = i + dx, j + dy
                if ((-1 < n_i < len(heights)) 
                    and (-1 < n_j < len(heights[0]))
                    and ((heights[i][j] <= heights[n_i][n_j]))
                    and (n_i, n_j) not in ocean):
                    dfs(n_i, n_j, ocean)

        for i in range(len(heights)):
            dfs(i, 0, pacific)

        for j in range(len(heights[0])):
            dfs(0, j, pacific)
        
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, atlantic)
        
        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, atlantic)

        return list(pacific & atlantic)
