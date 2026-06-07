class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, path_sum, idx):
            if  path_sum == target: 
                res.append(path[:])
                return
            if path_sum > target:
                return
            for i in range(idx, len(nums)):
                path.append(nums[i])
                path_sum += nums[i]
                backtrack(path, path_sum, i)
                path_sum -= nums[i]
                path.pop()
        
        backtrack([], 0, 0)
        return res