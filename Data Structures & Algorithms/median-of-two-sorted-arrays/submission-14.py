import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            n1, n2 = n2, n1
            nums1, nums2 = nums2, nums1

        total = n1 + n2
        half = total // 2
        l, r = 0, n1 - 1

        while True:
            mid1 = (l + r) // 2
            mid2 = half - mid1 - 2

            l1 = nums1[mid1] if mid1 > -1 else - math.inf
            l2 = nums2[mid2] if mid2 > -1 else - math.inf
            r1 = nums1[mid1 + 1] if mid1 + 1 < n1 else math.inf
            r2 = nums2[mid2 + 1] if mid2 + 1 < n2 else math.inf

            if l1 <= r2 and l2 <= r1:
                if total % 2 != 0:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1

        