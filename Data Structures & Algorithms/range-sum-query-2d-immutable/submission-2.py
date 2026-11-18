class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        self.sum_matrix = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                left = self.sum_matrix[i][j-1] if j > 0 else 0
                up = self.sum_matrix[i-1][j] if i > 0 else 0
                prev = self.sum_matrix[i-1][j-1] if i > 0 and j > 0 else 0
                self.sum_matrix[i][j] = left + up - prev + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        up = self.sum_matrix[row1-1][col2] if row1 > 0 else 0
        left = self.sum_matrix[row2][col1-1] if col1 > 0 else 0
        prev = self.sum_matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return self.sum_matrix[row2][col2] - left - up + prev
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)