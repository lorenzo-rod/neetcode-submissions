from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_counter = defaultdict(int)
        s_counter = defaultdict(int)

        for c in t:
            t_counter[c] += 1

        have, need = 0, len(t_counter)

        l = 0
        res = [0, len(s)]

        for r in range(len(s)):
            s_counter[s[r]] += 1

            if s[r] in t_counter and t_counter[s[r]] == s_counter[s[r]]:
                have += 1
            
            while have == need:
                if r - l < res[1] - res[0]:
                    res[0], res[1] = l, r

                s_counter[s[l]] -= 1

                if s[l] in t_counter and s_counter[s[l]] < t_counter[s[l]]:
                    have -= 1
                
                l += 1
        
        return s[res[0]: res[1] + 1] if res[1] < len(s) else ""

        