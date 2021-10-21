class Solution:
    def __init__(self):
        self.d = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "":
            return []
        
        # Backtracking
        def helper(digits, track):
            if digits == "":
                res.append("".join(track))
                return
            for l in self.d[digits[0]]:
                track.append(l)
                helper(digits[1:], track)
                track.pop()
                
        helper(digits, [])
        return res
            
        