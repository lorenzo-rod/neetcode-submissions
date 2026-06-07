class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        n = len(nums)
        target = total_sum // 2
        sum_set = set([0])
        
        for i in range(n):
            next_set = set()
            for t in sum_set:
                next_set.add(t + nums[i])
            sum_set |= next_set
            if target in sum_set:
                return True
        
        return False