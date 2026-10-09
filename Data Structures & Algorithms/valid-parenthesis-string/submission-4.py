class Solution:
    def checkValidString(self, s: str) -> bool:
        minimum = maximum = 0

        for c in s:
            if c == '(':
                minimum, maximum = minimum + 1, maximum + 1
            elif c == ')':
                minimum, maximum = minimum - 1, maximum - 1
            else:
                minimum, maximum = minimum - 1, maximum + 1
            if maximum < 0:
                return False
            minimum = max(minimum, 0)
        
        return minimum == 0
        