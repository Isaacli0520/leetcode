class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(s.strip().split()[::-1])
        arr = list(s)
        l, r = 0, len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
        def reverseWord(ll, rr):
            l, r = ll, rr
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            return "".join(arr[ll:rr + 1])
        
        res = []
        l = 0
        right_bound = len(arr) - 1
        while right_bound >= 0 and arr[right_bound] == " ":
            right_bound -= 1
        right_bound += 1
        while l < right_bound:
            while l < right_bound and arr[l] == " ":
                l += 1
            r = l
            while r < right_bound and arr[r] != " ":
                r += 1
            res.append(reverseWord(l, r - 1))
            l = r
        return " ".join(res)
            
        