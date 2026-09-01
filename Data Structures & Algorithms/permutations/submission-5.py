class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        visited = set()

        def backtrack(permutation):
            if len(permutation) == n:
                permutations.append(permutation[:])
            
            for i in range(n):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    permutation.append(nums[i])
                    backtrack(permutation)
                    permutation.pop()
                    visited.discard(nums[i])
        
        backtrack([])

        return permutations