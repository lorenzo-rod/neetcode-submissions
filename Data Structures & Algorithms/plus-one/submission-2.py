class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        i = len(digits) - 1

        while carry and i > -1:
            digits[i] += carry

            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
            
            i -= 1
        
        return [1] + digits if carry else digits
