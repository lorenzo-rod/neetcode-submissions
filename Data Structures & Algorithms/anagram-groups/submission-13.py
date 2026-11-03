from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)
        count = [0] * 26

        for s in strs:
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagrams[tuple(count)].append(s)
            for c in s:
                count[ord(c) - ord("a")] -= 1

        return list(anagrams.values())
        