class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals or len(intervals) == 1:
            return 0
        
        intervals = sorted(intervals, key = lambda x: x[1])
        
        total_count = len(intervals)
        count = 0
        
        current_end = -float('inf')
        for i in range(total_count):
            if intervals[i][0] >= current_end:
                current_end = intervals[i][1]
                count += 1

        return total_count-count
        