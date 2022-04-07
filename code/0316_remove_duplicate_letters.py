class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {}
        for i, c in enumerate(s):
            last_occ[c] = i
        stack = []
        visited = set()
        for i, c in enumerate(s):
            if c not in visited:
                # If last item in stack is bigger than c and it's gonna
                # appear later, we pop it from the stack and remove from visited
                while stack and stack[-1] > c and last_occ[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(c)
                visited.add(c)
        return "".join(stack)