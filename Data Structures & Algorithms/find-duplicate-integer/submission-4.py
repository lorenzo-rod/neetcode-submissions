class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        arr = [0] * (len(nums))

        for num in nums:
            arr[num - 1] += 1
            if arr[num - 1] == 2:
                return num