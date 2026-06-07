class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = [0] * 26
        counter = [0] * 26
        n = len(s1)
        left = 0
        right = n - 1
        
        for c in s1:
            counter_s1[ord(c) - ord("a")] += 1
        
        for c in s2[left:right+1]:
            counter[ord(c) - ord("a")] += 1
    
        if counter == counter_s1:
            return True

        for right in range(n, len(s2)):
            counter[ord(s2[left]) - ord("a")] -= 1
            counter[ord(s2[right]) - ord("a")] += 1

            if counter == counter_s1:
                return True
            
            left += 1
        
        return False

