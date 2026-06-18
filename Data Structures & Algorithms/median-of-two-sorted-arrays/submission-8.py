import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        if m < n:
            m, n = n, m
            nums1, nums2 = nums2, nums1
        
        total = m + n
        half = total // 2

        l, r = 0, n - 1

        while True:
            mid1 = (l + r) // 2
            mid2 = half - mid1 - 2

            left1 = nums1[mid1] if mid1 > -1 else - math.inf
            left2 = nums2[mid2] if mid2 > -1 else - math.inf
            right1 = nums1[mid1+1] if mid1 + 1 < n else math.inf
            right2 = nums2[mid2+1] if mid2 + 1 < m else math.inf

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (min(right1, right2) + max(left1, left2)) / 2
                else:
                    return min(right1, right2)
            elif left1 > right2:
                r = mid1 - 1
            else:
                l = mid1 + 1
