class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        def helper(i, path):
            if i == len(digits):
                res.append("".join(path))
                return
            for letter in d[digits[i]]:
                path.append(letter)
                helper(i + 1, path)
                path.pop()
        
        helper(0, [])
        return res