class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m, n = len(matrix), len(matrix[0])
        row_zero = False
        column_zero = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if i == 0:
                        column_zero = True
                    if j == 0:
                        row_zero = True
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if row_zero:
            for i in range(m):
                matrix[i][0] = 0
        
        if column_zero:
            for j in range(n):
                matrix[0][j] = 0
