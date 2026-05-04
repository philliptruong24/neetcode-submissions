class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ')' and stack:
                if '(' != stack.pop():
                    return False
            elif i == '}' and stack:
                if '{' != stack.pop():
                    return False
            elif i == ']' and stack:
                if '[' != stack.pop():
                    return False
            else:
                stack.append(i)
    
        if stack:
            return False
        return True
