import string
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        def helper(s, track):
            if not s:
                res.append(track)
                return
            if s[0] in string.ascii_lowercase:
                helper(s[1:], track + s[0].upper())
            if s[0] in string.ascii_uppercase:
                helper(s[1:], track + s[0].lower())
            helper(s[1:], track + s[0])
        helper(S, "")
        return res