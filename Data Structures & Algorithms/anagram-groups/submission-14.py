from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def idx(c):
            return ord(c) - ord("a")
        
        anagrams = defaultdict(list)

        for s in strs:
            identifier = [0] * 26

            for c in s:
                identifier[idx(c)] += 1
            
            anagrams[tuple(identifier)].append(s)
        
        return list(anagrams.values())
