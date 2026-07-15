class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def backtrack(permutation):
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                permutation.append(nums[i])
                seen.add(nums[i])
                backtrack(permutation)
                seen.discard(nums[i])
                permutation.pop()
        
        backtrack([])
        return res