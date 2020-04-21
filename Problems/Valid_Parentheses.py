# Runtime : 20 ms
# Memory Usage : 14 MB
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')' and len(stack) >= 1:
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
            elif s[i] == ']' and len(stack) >= 1:
                if stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False
            elif s[i] == '}' and len(stack) >= 1:
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
        if len(stack) >= 1:
            return False
        return True
