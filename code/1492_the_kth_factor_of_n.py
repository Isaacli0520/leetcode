class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f1, f2 = [], []
        cnt = 0
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                cnt += 1
                f1.append(i)
                f2.append(n // i)
                if cnt == k:
                    return i
        
        if f1[-1] == f2[-1]:
            f2.pop()
        f2 = f2[::-1]
        return f2[k - cnt - 1] if k - cnt <= len(f2) else -1
            