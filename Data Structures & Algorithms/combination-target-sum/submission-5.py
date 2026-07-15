class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(combination, total, start):
            if total == target:
                res.append(combination[:])
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                combination.append(nums[i])
                total += nums[i]
                backtrack(combination, total, i)
                total -= nums[i]
                combination.pop()
            
        backtrack([], 0, 0)
        return res