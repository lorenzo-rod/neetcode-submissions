class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m = len(matrix)
        n = len(matrix[0])
        right = m * n - 1
        while(left < right):
            mid = (left + right) // 2
            i = mid // n
            j = mid % n
            print(i, j, mid)
            if (matrix[i][j] < target):
                left = mid + 1
            elif matrix[i][j] == target:
                return True
            else:
                right = mid
        return matrix[left // n][left % n] == target