class Solution:
    # Greedy
    # 
    # Always pick the one with the earliest end time because 
    # this provides the maximum rest intervals for us to pick
    # the next interval. Suppose we have a somewhat later interval
    # with bigger end, it will have at least one less interval
    # for us to choose from.
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # cnt of nonoverlapping intervals
        cnt = 1
        intervals = sorted(intervals, key=lambda x:x[1])
        curr_end = intervals[0][1]
        for start, end in intervals:
            if start >= curr_end:
                cnt += 1
                curr_end = end
        return len(intervals) - cnt
        