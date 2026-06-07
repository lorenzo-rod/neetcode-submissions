class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        left, right = 0, 0
        max_length = 0

        for i in range(len(s)):
            l, r = i, i
            length = 0
            while(l > -1 and r < len(s) and s[l] == s[r]):
                length = r - l + 1
                if length > max_length:
                    max_length = length
                    left = l
                    right = r
                l -= 1
                r += 1
            
            l, r = i, i + 1
            length = 0
            while(l > -1 and r < len(s) and s[l] == s[r]):
                length = r - l + 1
                if length > max_length:
                    max_length = length
                    left = l
                    right = r
                l -= 1
                r += 1

        return s[left:right+1]