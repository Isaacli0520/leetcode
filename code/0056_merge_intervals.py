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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        itvs = sorted(intervals, key=lambda x:(x[0], -x[1]))
        
        res = []
        left, right = itvs[0]
        for itv in itvs:
            # cover
            if itv[1] <= right:
                pass
            # overlap
            elif itv[1] > right and itv[0] <= right:
                right = itv[1]
            # separate
            elif itv[0] > right:
                res.append((left, right))
                left, right = itv
        res.append((left, right))
        return res