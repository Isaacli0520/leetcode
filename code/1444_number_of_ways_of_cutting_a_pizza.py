class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        r, c = len(pizza), len(pizza[0])
        # add padding to help initialize
        arr = [[0] * (c + 1) for i in range(r + 1)]
        
        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                arr[i][j] = int(pizza[i][j] == "A") + arr[i + 1][j] + arr[i][j + 1] - arr[i + 1][j + 1]
                
        dp = {}
        def helper(si, sj, cnt):
            if (si, sj, cnt) in dp:
                return dp[(si, sj, cnt)]
            
            # no apples, early stop
            if arr[si][sj] == 0:
                return 0
            # no need to cut if there is at least 1 apple
            # and we only need 1 apple
            if cnt == 1:
                return 1
            
            tmp = 0
            # horizontal
            for i in range(si + 1, r):
                # make sure we at least cut one apple
                if arr[i][sj] < arr[si][sj]:
                    tmp = (tmp + helper(i, sj, cnt - 1)) % 1000000007
                    
            # vertical
            for j in range(sj + 1, c):
                # make sure we at least cut one apple
                if arr[si][j] < arr[si][sj]:
                    tmp = (tmp + helper(si, j, cnt - 1)) % 1000000007
            dp[(si, sj, cnt)] = tmp
            return tmp
        
        return helper(0, 0, k) 
