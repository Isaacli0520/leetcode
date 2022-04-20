class Solution:
    # 0. j++
    #      ---
    #  ---
    # 1. j++
    #    ---
    #  ---
    # 2. j++
    #    -----
    #     ---
    # 3. i++
    #    ---
    #   -----
    # 4. i++
    #    ----
    #      ----
    # 5. i++
    #    ---
    #         ----
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a, b = firstList[i], secondList[j]
            left, right = max(a[0], b[0]), min(a[1], b[1])
            if left <= right:
                res.append((left, right))
            if b[1] >= a[1]:
                i += 1
            else:
                j += 1
            # if b[1] < a[0]:
            #     j += 1
            # elif b[1] >= a[0] and b[1] <= a[1] and b[0] < a[0]:
            #     res.append((a[0], b[1]))
            #     j += 1
            # elif b[0] >= a[0] and b[1] <= a[1]:
            #     res.append(b)
            #     j += 1
            # elif a[0] >= b[0] and a[1] <= b[1]:
            #     res.append(a)
            #     i += 1
            # elif b[0] <= a[1] and b[1] > a[1]:
            #     res.append((b[0], a[1]))
            #     i += 1
            # elif b[0] > a[1]:
            #     i += 1
        return res