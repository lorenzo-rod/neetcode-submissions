class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        target = abs(target)
        total = sum(nums)

        n = len(nums) + 1
        m = 2 * (total) + 1

        row = [0] * (m)
        prev_row = row[:]
        prev_row[total] = 1

        for i in reversed(range(n - 1)):
            for j in reversed(range(m)):
                if -1 < j - nums[i]:
                    a = prev_row[j - nums[i]]
                else:
                    a = 0
                if j + nums[i] < m:
                    b = prev_row[j + nums[i]]
                else:
                    b = 0
                row[j] = a + b
            prev_row = row[:]
        

        return row[total - target] if total - target > -1 else 0
