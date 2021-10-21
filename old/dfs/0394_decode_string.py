class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        tmp_str = ""
        tmp_num = 0
        for char in s:
            if char == "[":
                # Push str so far to the stack
                stack.append(tmp_str)
                # Push num for next tmp_str to the stack
                stack.append(tmp_num)
                tmp_str = ""
                tmp_num = 0
            if char == "]":
                num = stack.pop()
                prev_str = stack.pop()
                tmp_str = prev_str + num * tmp_str
            if char.isdigit():
                tmp_num = tmp_num * 10 + int(char)
            if char.isalpha():
                tmp_str += char
        return tmp_str