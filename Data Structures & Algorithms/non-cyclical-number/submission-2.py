class Solution:
    def isHappy(self, n: int) -> bool:

        def squareDigits(n):
            number = 0
            while n:
                number += (n % 10) ** 2
                n = n // 10
            return number

        slow = n
        fast = squareDigits(n)

        while slow != 1 and slow != fast:
            slow = squareDigits(slow)
            fast = squareDigits(squareDigits(fast))
        
        return slow == 1
            