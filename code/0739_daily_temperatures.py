class Solution:
    # Decreasing Monotonic Stack 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []
        
        # Push index to stack instead of temperature
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1] - i)
            stack.append(i)
        return res[::-1]