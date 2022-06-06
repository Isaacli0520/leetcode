class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        cnt = 0
        for i in range(2, n):
            if isPrime[i]:
                cnt += 1
        return cnt