class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod, max_prod = 1, 1
        maximum = nums[0]
        
        for num in nums:
            tmp = max_prod * num
            max_prod = max(num, tmp, min_prod * num)
            min_prod = min(num, tmp, min_prod * num)
            maximum = max(maximum, max_prod)
        
        return maximum