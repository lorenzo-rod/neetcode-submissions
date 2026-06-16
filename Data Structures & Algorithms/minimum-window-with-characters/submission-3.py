from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        char_count_t = defaultdict(int)
        char_count_s = defaultdict(int)
        res = [0, len(s)]

        for c in t:
            char_count_t[c] += 1

        have, need = 0, len(char_count_t)

        l = 0

        for r in range(len(s)):
            c = s[r]
            char_count_s[c] += 1

            if c in char_count_t and char_count_s[c] == char_count_t[c]:
                have += 1
            
            while have == need:
                if r - l < res[1] - res[0]:
                    res[0], res[1] = l, r
                
                char_count_s[s[l]] -= 1

                if s[l] in char_count_t:
                    if char_count_s[s[l]] < char_count_t[s[l]]:
                        have -= 1
                
                l += 1
            
        return s[res[0]: res[1] + 1] if res[1] < len(s) else ""



        
