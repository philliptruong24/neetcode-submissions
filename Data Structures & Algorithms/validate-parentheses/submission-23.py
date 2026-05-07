class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pair = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        for i in s:
            if i in bracket_pair:
                if stack and stack[-1] == bracket_pair[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return not stack


