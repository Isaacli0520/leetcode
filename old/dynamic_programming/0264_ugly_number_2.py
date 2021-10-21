class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        nums = [1]
        # Pointers for 2, 3, 5
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            # Move pointer for the smallest next number
            # And append to list
            a, b, c = nums[p2]*2, nums[p3]*3, nums[p5]*5
            curr = min(a,b,c)
            if curr == a:
                p2 += 1
            if curr == b:
                p3 += 1
            if curr == c:
                p5 += 1
            nums.append(curr)
        return nums[-1]