class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
            
        res = "".join(sorted(map(str, nums), key=cmp_to_key(cmp)))
        return "0" if res[0] == "0" else res