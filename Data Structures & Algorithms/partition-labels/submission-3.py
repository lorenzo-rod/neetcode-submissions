class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []

        last_index = {}

        for i, c in enumerate(s):
            last_index[c] = i

        end = 0
        size = 0
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])

            if end == i:
                res.append(size)
                size = 0
        
        return res
        