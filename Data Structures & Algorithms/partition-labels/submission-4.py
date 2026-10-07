class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []

        last_index = [0] * 26

        for i, c in enumerate(s):
            last_index[ord(c) - ord("a")] = i

        end = 0
        size = 0
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[ord(c) - ord("a")])

            if end == i:
                res.append(size)
                size = 0
        
        return res
        