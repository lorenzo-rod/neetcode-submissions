class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        identifier = [0] * 26
        for word in strs:
            for c in word:
                identifier[ord(c) - ord("a")] += 1
            if tuple(identifier) not in anagram_groups:
                anagram_groups[tuple(identifier)] = [word]
            else:
                anagram_groups[tuple(identifier)].append(word)
            for i in range(26):
                identifier[i] = 0
        return list(anagram_groups.values())