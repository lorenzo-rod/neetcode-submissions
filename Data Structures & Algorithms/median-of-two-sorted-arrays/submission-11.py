import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        if n > m:
            n, m = m, n
            nums1, nums2 = nums2, nums1

        l, r = 0, n - 1
        total = m + n
        half = total // 2
        
        while True:
            mid1 = (l + r) // 2
            mid2 = half - mid1 - 2

            l1 = nums1[mid1] if mid1 > -1 else - math.inf
            l2 = nums2[mid2] if mid2 > -1 else - math.inf
            r1 = nums1[mid1 + 1] if mid1 < n - 1 else math.inf
            r2 = nums2[mid2 + 1] if mid2 < m - 1 else math.inf

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 1:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1

