class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []

        counter = [0] * 26

        for c in s:
            counter[ord(c) - ord("a")] += 1
        
        letters = set()
        start = 0

        for end, c in enumerate(s):
            letters.add(c)
            counter[ord(c) - ord("a")] -= 1

            if all(counter[ord(letter) - ord("a")] == 0 for letter in letters):
                res.append(end - start + 1)
                start = end + 1
                letters.clear()
        
        return res
