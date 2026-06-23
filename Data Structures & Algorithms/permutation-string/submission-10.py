class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        char_count1 = [0] * 26
        char_count2 = [0] * 26
        matches = 0

        for i, c in enumerate(s1):
            char_count1[ord(c) - ord("a")] += 1
            char_count2[ord(s2[i]) - ord("a")] += 1
        
        for i in range(26):
            if char_count1[i] == char_count2[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        l = 0

        for r in range(len(s1), len(s2)):
            l_index = ord(s2[l]) - ord("a")
            r_index = ord(s2[r]) - ord("a")

            char_count2[l_index] -= 1
            if char_count2[l_index] + 1 == char_count1[l_index]:
                matches -= 1
            elif char_count2[l_index] == char_count1[l_index]:
                matches += 1
            
            char_count2[r_index] += 1
            if char_count2[r_index] == char_count1[r_index]:
                matches += 1
            elif char_count2[r_index] - 1 == char_count1[r_index]:
                matches -= 1
            
            if matches == 26:
                return True
            
            l += 1
        
        return False


