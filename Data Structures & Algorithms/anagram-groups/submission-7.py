from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        count = [0] * 26
        for s in strs:
            for i in range(26):
                count[i] = 0
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())