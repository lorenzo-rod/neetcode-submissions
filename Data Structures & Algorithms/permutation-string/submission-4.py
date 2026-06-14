class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        char_count1 = [0] * 26
        char_count2 = [0] * 26
        matches = 0

        for i, c in enumerate(s1):
            char_count1[ord(c) - ord("a")] += 1
            char_count2[ord(s2[i]) - ord("a")] += 1
        
        for a, b in zip(char_count1, char_count2):
            if a == b:
                matches += 1
        
        if matches == 26:
            return True
        
        l = 0

        for r in range(len(s1), len(s2)):

            char_count2[ord(s2[l]) - ord("a")] -= 1

            if char_count2[ord(s2[l]) - ord("a")] == char_count1[ord(s2[l]) - ord("a")]:
                matches += 1
            elif char_count2[ord(s2[l]) - ord("a")] + 1 == char_count1[ord(s2[l]) - ord("a")]:
                matches -= 1

            char_count2[ord(s2[r]) - ord("a")] += 1

            if char_count2[ord(s2[r]) - ord("a")] == char_count1[ord(s2[r]) - ord("a")]:
                matches += 1
            elif char_count2[ord(s2[r]) - ord("a")] - 1 == char_count1[ord(s2[r]) - ord("a")]:
                matches -= 1

            if matches == 26:
                return True
            
            l += 1
        
        return False

