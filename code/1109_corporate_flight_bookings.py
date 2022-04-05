class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Construct diff array
        diff = [0] * n
        for bk in bookings:
            start, end, seats = bk
            diff[start - 1] += seats
            if end < n:
                diff[end] -= seats
        # Restore org array
        for i in range(1, len(diff)):
            diff[i] += diff[i - 1]
        return diff