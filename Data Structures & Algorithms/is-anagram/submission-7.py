class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)

        if n1 != n2:
            return False
        
        def idx(c):
            return ord(c) - ord("a")
        
        s_counter = [0] * 26
        t_counter = [0] * 26

        for i in range(n1):
            s_counter[idx(s[i])] += 1
            t_counter[idx(t[i])] += 1

        return s_counter == t_counter
        