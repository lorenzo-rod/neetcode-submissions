class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i, c in enumerate(s1):
            s1_count[ord(c) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for a, b in zip(s1_count, s2_count):
            if a == b:
                matches += 1
        
        if matches == 26:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            left_index = ord(s2[l]) - ord("a")
            right_index = ord(s2[r]) - ord("a")

            s2_count[left_index] -= 1

            if s2_count[left_index] == s1_count[left_index]:
                matches += 1
            elif s2_count[left_index] + 1 == s1_count[left_index]:
                matches -= 1

            s2_count[right_index] += 1

            if s2_count[right_index] == s1_count[right_index]:
                matches += 1
            elif s2_count[right_index] - 1 == s1_count[right_index]:
                matches -= 1

            if matches == 26:
                return True
            
            l += 1

        return False