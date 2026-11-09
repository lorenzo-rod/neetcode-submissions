from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        counter1 = [0] * 26
        counter2 = [0] * 26

        def idx(c):
            return ord(c) - ord("a")

        for c in s1:
            counter1[idx(c)] += 1

        for i in range(len(s1)):
            counter2[idx(s2[i])] += 1

        if counter1 == counter2:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            counter2[idx(s2[l])] -= 1
            counter2[idx(s2[r])] += 1

            if counter1 == counter2:
                return True

            l += 1

        return False
