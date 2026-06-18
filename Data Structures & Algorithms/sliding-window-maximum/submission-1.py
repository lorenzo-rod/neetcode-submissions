from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)

        k_count = defaultdict(int)

        for num in nums[:k]:
            k_count[num] += 1

        # print(k_count)

        maximum = max(k_count.keys())
        res[0] = maximum

        l = 0

        for r in range(k, len(nums)):
            k_count[nums[r]] += 1
            k_count[nums[l]] -= 1

            if k_count[nums[l]] == 0:
                del k_count[nums[l]]

            if nums[r] > maximum:
                maximum = nums[r]
            elif nums[l] == maximum:
                if nums[l] not in k_count:
                    maximum = max(k_count.keys())
            
            l += 1
            # print(l, res, maximum)
            res[l] = maximum
        
        return res