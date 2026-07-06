class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(combination, total, start):
            if total == target:
                res.append(combination[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                combination.append(candidates[i])
                total += candidates[i]
                backtrack(combination, total, i + 1)
                total -= candidates[i]
                combination.pop()
        
        backtrack([], 0, 0)
        return res