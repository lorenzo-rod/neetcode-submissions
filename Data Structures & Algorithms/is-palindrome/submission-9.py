class Solution:
    def isPalindrome(self, s: str) -> bool:
         
        l, r = 0, len(s) - 1

        while l < r:
            
            if s[l] == " " or not s[l].isalnum():
                l += 1
            elif s[r] == " " or not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        
        return True
