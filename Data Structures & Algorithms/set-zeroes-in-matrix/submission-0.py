class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        positions = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    positions.add((i,j))
        
        for pos in positions:
            for i in range(m):
                matrix[i][pos[1]] = 0
            for j in range(n):
                matrix[pos[0]][j] = 0
        