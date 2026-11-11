class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def idx(c):
            return ord(c) - ord("A")

        t_counter = [0] * 100
        s_counter = [0] * 100

        for c in t:
            t_counter[idx(c)] += 1

        res = [0, len(s)]
        
        have, need = 0, 0

        for num in t_counter:
            if num > 0:
                need += 1

        l = 0

        for r in range(len(s)):
            s_counter[idx(s[r])] += 1

            if t_counter[idx(s[r])] > 0 and s_counter[idx(s[r])] == t_counter[idx(s[r])]:
                have += 1

            while have == need:
                
                if r - l < res[1] - res[0]:
                    res[0], res[1] = l, r

                if t_counter[idx(s[l])] > 0 and s_counter[idx(s[l])] == t_counter[idx(s[l])]:
                    have -= 1
                
                s_counter[idx(s[l])] -= 1
                l += 1
        
        return s[res[0] : res[1] + 1] if res[1] < len(s) else ""
