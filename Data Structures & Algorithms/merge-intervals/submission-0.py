class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda interval: interval[0])
        prev_interval = intervals[0]
        for i, interval in enumerate(intervals):
            if interval[0] > prev_interval[1]:
                res.append(prev_interval)
                prev_interval = interval
            else:
                prev_interval = [
                    min(prev_interval[0], interval[0]),
                    max(prev_interval[1], interval[1]),
                ]

        res.append(prev_interval)
        return res
