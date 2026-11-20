class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, n - 1
            target = - nums[i]
            while l < r:

                total = nums[l] + nums[r]

                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    res.append([nums[l], nums[r], nums[i]])

                    l += 1
                    while l < n and nums[l] == nums[l-1]:
                        l += 1
                    
                    r -= 1
                    while r > -1 and nums[r] == nums[r+1]:
                        r -= 1
        
        return res
