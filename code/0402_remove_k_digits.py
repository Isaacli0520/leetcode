class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and k > 0:
                if stack[-1] > num[i] :
                    stack.pop()
                    k -= 1
                else:
                    break
            stack.append(num[i])
            
        while k > 0:
            stack.pop()
            k -= 1
            
        i = 0
        while i < len(stack):
            if stack[i] != "0":
                break
            i += 1
        res = "".join(stack[i:])
        return res if res else "0"
        
        