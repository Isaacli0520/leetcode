class Solution:
    # Sort by start in ascending order and then end in descending order
    # Three cases:
    # 1. cover
    #   -----
    #    ---
    # 2. overlap
    #   ----
    #     ----
    # 3. separate
    #   ---
    #        ----
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        itvs = sorted(intervals, key=lambda x:(x[0], -x[1]))
        
        res = 0
        right = itvs[0][1]
        for i in range(1, len(itvs)):
            itv = itvs[i]
            # 1. cover
            if itv[1] <= right:
                res += 1
            else:
                right = itv[1]
            # # 2. overlap
            # elif itv[0] <= right and itv[1] > right:
            #     right = itv[1]
            # # 3. separate
            # elif itv[0] > right:
            #     right = itv[1]
        return len(itvs) - res
            