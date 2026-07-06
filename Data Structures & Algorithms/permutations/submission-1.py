class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(permutation, seen):
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                permutation.append(nums[i])
                seen.add(nums[i])
                backtrack(permutation, seen)
                seen.discard(nums[i])
                permutation.pop()
        
        backtrack([], set())
        return res