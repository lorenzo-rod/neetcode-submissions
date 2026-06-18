from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)
        l = 0
        q = deque()

        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                # print("popping", q)
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                res[l] = nums[q[0]]
                l += 1

            # print(q) 
        
        return res