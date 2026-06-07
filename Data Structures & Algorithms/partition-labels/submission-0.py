class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        res = []

        for i, c in enumerate(s):
            last_index[c] = i

        size = end = 0

        for i in range(len(s)):
            size += 1
            end = max(end, last_index[s[i]])

            if end == i:
                res.append(size)
                size = 0

        return res
        