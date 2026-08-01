class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        freqs = [0] * (n + 1)

        for num in nums:
            if freqs[num] > 0:
                return num
            else:
                freqs[num] += 1
                 