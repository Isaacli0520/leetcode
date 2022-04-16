class Solution:
    def __init__(self):
        self.d = {}
        
    def diffWaysToCompute(self, expression: str) -> List[int]: 
        if expression in self.d:
            return self.d[expression]
        res = []
        for i, char in enumerate(expression):
            if char in ["+", "-", "*"]:
                left = self.diffWaysToCompute("".join(expression[:i]))
                right = self.diffWaysToCompute("".join(expression[i + 1:]))
                for l in left:
                    for r in right:
                        if char == "+":
                            res.append(l + r)
                        elif char == "-":
                            res.append(l - r)
                        elif char == "*":
                            res.append(l * r)
        if not res:
            self.d[expression] = [int(expression)]
            return [int(expression)]
        self.d[expression] = res
        return res