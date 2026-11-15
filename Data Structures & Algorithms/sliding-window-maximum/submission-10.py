from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        res = [0] * (n - k + 1)
        l = 0
        q = deque()

        for r in range(n):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r >= k - 1:
                res[l] = nums[q[0]]
                l += 1
        
        return res
        