class Solution:
    # Greedy
    # sort by start, and for same start, bigger end comes first
    # As long as the start of a clip covers, we want to choose the
    # biggest end.
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = sorted(clips, key=lambda x:(x[0], -x[1]))
        i = 0
        curr_end = 0
        next_end = 0
        res = 0
        # if curr clip can't even cover the furthest end by far,
        # then this task is impossible
        while i < len(clips) and clips[i][0] <= curr_end:
            # Find the next clip that covers current end and has
            # the biggest end
            while i < len(clips) and clips[i][0] <= curr_end:
                next_end = max(next_end, clips[i][1])
                i += 1
            curr_end = next_end
            res += 1
            if curr_end >= time:
                return res
        return -1