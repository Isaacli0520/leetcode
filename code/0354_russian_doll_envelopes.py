from functools import cmp_to_key

class Solution:
    # Similar to Longest Increasing Subsequence
    #
    # How to squeeze 2D to 1D?
    # 
    #   sort envelopes by width first, for same width, sort by h in 
    #   descending order because same width or height envelopes can't fit
    #
    #   solve LIS on the list of envelopes with regard to their heights
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def cmp(a, b):
            if a[0] - b[0] == 0:
                return b[1] - a[1]
            return a[0] - b[0]
        ls = [item[1] for item in sorted(envelopes, key=cmp_to_key(cmp))]
        
        # LIS Binary Search version O(nlogn)
        tops = []
        for i in range(len(ls)):
            card = ls[i]
            left, right = 0, len(tops)
            while left < right:
                mid = left + (right - left) // 2
                if tops[mid] < card:
                    left = mid + 1
                elif tops[mid] >= card:
                    right = mid
            if left == len(tops):
                tops.append(card)
            else:
                tops[left] = card
        return len(tops)
        