class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        count = 0

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            elif prev_end > start:
                count += 1
                prev_end = min(end, prev_end)
        
        return count
