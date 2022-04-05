class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0]
        for trip in trips:
            num, start, end = trip
            if end + 1 > len(diff):
                diff += [0] * (end - len(diff) + 1)
            diff[start] += num
            if end < len(diff):
                diff[end] -= num
        
        if diff[0] > capacity:
            return False
        for i in range(1, len(diff)):
            diff[i] += diff[i - 1]
            if diff[i] > capacity:
                return False
        return True
        