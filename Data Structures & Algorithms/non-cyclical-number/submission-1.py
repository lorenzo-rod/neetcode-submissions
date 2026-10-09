class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()

        number = 0

        while True:
            while n:
                number += (n % 10) ** 2
                n = n // 10
            
            if number == 1:
                return True

            if number in numbers:
                return False
            
            numbers.add(number)
            n = number
            number = 0
