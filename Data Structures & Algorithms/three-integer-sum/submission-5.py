class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if (i > 0 and num == nums[i-1]):
                continue
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                nums_sum = nums[left] + nums[right] + num
                if nums_sum < 0:
                    left += 1
                elif nums_sum > 0:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while(left < right and nums[left] == nums[left-1]):
                        left += 1
        return res