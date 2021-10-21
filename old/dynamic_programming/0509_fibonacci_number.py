class Solution:
    def fib(self, N: int) -> int:
        prev, curr = 1, 0
        for i in range(N):
            curr, prev = curr + prev, curr
        return curr