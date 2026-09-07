class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        n = len(intervals)
        new_interval = intervals[0]

        for i in range(1, n):
            if new_interval[1] < intervals[i][0]:
                res.append(new_interval)
                new_interval = intervals[i]
            else:
                new_interval[1] = max(new_interval[1], intervals[i][1])

        res.append(new_interval)
        return res
