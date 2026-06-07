class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        seen = set()

        def backtrack(path, counter):
            if tuple(counter) in seen:
                return
            path_sum = sum(path)
            if path_sum > target:
                return
            if  path_sum == target: 
                res.append(path[:])
                seen.add(tuple(counter))
                return
            for num in nums:
                path.append(num)
                counter[num] += 1
                backtrack(path, counter)
                counter[num] -= 1
                path.pop()
        
        backtrack([], [0] * 30)
        return res