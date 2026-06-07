class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = n - 1
            target = -nums[i]
            while(l < r):
                nums_sum = nums[l] + nums[r]
                if nums_sum > target:
                    r -= 1
                elif nums_sum < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res
            
                    
