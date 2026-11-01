class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []

        last_index = [0] * 26

        for i, c in enumerate(s):
            last_index[ord(c) - ord("a")] = i
        
        start = 0
        end = 0
        i = 0

        for i in range(len(s)):
            end = max(last_index[ord(s[i]) - ord("a")], end)

            if i == end:
                res.append(end - start + 1)
                start = end + 1
        
        return res
