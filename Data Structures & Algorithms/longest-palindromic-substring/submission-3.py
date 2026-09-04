class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_l, max_r = 0, 0
        n = len(s)
        max_distance = 0

        for i in range(n):
            l, r = i, i

            while l > -1 and r < n and s[l] == s[r]:
                distance = r - l

                if distance > max_distance:
                    max_distance = distance
                    max_l, max_r = l, r

                l, r = l - 1, r + 1

            l, r = i, i+1

            while l > -1 and r < n and s[l] == s[r]:
                distance = r - l

                if distance > max_distance:
                    max_distance = distance
                    max_l, max_r = l, r

                l, r = l - 1, r + 1
        
        return s[max_l: max_r + 1]


                