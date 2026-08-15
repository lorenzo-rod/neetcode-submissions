class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        if isPalindrome(s):
            return True
        
        for i in range(len(s)):
            if isPalindrome(s[0:i] + s[i+1:]):
                return True
        
        return False
        

