class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        n = len(matrix[0])
        right = len(matrix) * n - 1
        while(left < right):
            mid = (left + right) // 2
            if (matrix[mid // n][mid % n] < target):
                left = mid + 1
            else:
                right = mid
        return matrix[left // n][left % n] == target