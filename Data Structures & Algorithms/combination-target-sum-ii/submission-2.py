class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(path, path_sum, start):
            if path_sum == target:
                res.append(path[:])
                return
            if path_sum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(path, path_sum + candidates[i], i + 1)
                path.pop()
        
        backtrack([], 0, 0)
        return res