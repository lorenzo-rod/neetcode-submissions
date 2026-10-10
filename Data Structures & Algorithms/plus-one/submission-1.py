class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        i = len(digits) - 1

        for digit in reversed(digits):
            digit += carry

            if digit == 10:
                digit = 0
                carry = 1
            else:
                carry = 0
            
            digits[i] = digit
            i -= 1

            if not carry:
                break
        
        return [1] + digits if carry else digits
