class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        explored_pacific = set()
        explored_atlantic = set()

        def dfs(i, j, explored):
            for dx, dy in directions:
                n_i, n_j = i + dx, j + dy
                if (
                    -1 < n_i < m
                    and -1 < n_j < n
                    and heights[n_i][n_j] >= heights[i][j]
                    and (n_i, n_j) not in explored
                ):
                    explored.add((n_i, n_j))
                    dfs(n_i, n_j, explored)

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0) and (i, j) not in explored_pacific:
                    explored_pacific.add((i, j))
                    dfs(i, j, explored_pacific)
                if (i == m - 1 or j == n - 1) and (i, j) not in explored_atlantic:
                    explored_atlantic.add((i, j))
                    dfs(i, j, explored_atlantic)

        return [list(pos) for pos in explored_pacific & explored_atlantic]
