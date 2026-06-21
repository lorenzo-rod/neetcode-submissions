from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums_counter = defaultdict(int)

        for num in nums:
            nums_counter[num] += 1
            if nums_counter[num] == 2:
                return num
