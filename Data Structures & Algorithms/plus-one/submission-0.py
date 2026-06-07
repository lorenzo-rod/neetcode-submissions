class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in reversed(range(len(digits))):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                break
        
        if i == 0 and digits[0] == 0:
            return [1] + digits
        
        return digits