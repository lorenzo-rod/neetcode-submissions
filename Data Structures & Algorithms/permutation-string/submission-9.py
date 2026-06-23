class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        char_count1 = [0] * 26
        char_count2 = [0] * 26

        for i, c in enumerate(s1):
            char_count1[ord(c) - ord("a")] += 1
            char_count2[ord(s2[i]) - ord("a")] += 1
        
        if char_count1 == char_count2:
            return True
        
        l = 0

        for r in range(len(s1), len(s2)):
            char_count2[ord(s2[l]) - ord("a")] -= 1
            l += 1

            char_count2[ord(s2[r]) - ord("a")] += 1

            if char_count1 == char_count2:
                return True
        
        return False