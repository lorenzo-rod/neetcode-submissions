class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        m = len(matrix)
        n = len(matrix[0])
        r = m * n
        while l < r:
            mid = (l + r) // 2
            if matrix[mid // (n)][mid % (n)] < target:
                l = mid + 1
            else:
                r = mid
        
        return l <= ((m * n) - 1) and matrix[l // (n)][l % (n)] == target
