from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s = Counter(s)
        counter_t = Counter(t)

        for c in s:
            if c not in counter_t:
                return False
            if counter_s[c] != counter_t[c]:
                return False
        
        return True