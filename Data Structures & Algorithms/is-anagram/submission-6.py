class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = [0] * 26

        n = len(s)

        for i in range(n):
            s_list[ord(s[i]) - ord("a")] += 1
            s_list[ord(t[i]) - ord("a")] -= 1
        
        for i in s_list:
            if i != 0:
                return False
        
        return True
