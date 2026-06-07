class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(path, seen):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if nums[i] in seen:
                    continue
                path.append(nums[i])
                seen.add(nums[i])
                backtrack(path, seen)
                seen.discard(nums[i])
                path.pop()
        
        backtrack([], set())
        return res