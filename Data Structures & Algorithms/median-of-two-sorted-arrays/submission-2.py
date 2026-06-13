import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        
        if m < n:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        half = (m + n) // 2
        total = m + n

        l, r = 0, n - 1

        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            left1 = nums1[m1] if m1 >= 0 else - math.inf
            left2 = nums2[m2] if m2 >= 0 else - math.inf
            right1 = nums1[m1 + 1] if (m1 + 1) < n else math.inf
            right2 = nums2[m2 + 1] if (m2 + 1) < m else math.inf

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return min(right1, right2)
            elif left1 > right2:
                r = m1 - 1
            else:
                l = m1 + 1
            
