from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = defaultdict(list)

        for s in strs:
            identifier = [0] * 26
            for c in s:
                identifier[ord(c) - ord("a")] += 1
            anagrams[tuple(identifier)].append(s)
        
        return list(anagrams.values())