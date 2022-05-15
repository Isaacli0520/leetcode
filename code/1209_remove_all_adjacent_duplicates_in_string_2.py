class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            # Merge or append
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            # If top of stack has k duplicate letters, pop it
            if stack[-1][1] == k:
                stack.pop()
            
        return "".join(c * f for c, f in stack)