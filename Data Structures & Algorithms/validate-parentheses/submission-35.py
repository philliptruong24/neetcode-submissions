class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketpair = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i in range(len(s)):
            if s[i] in bracketpair:
                if not stack or (stack and stack.pop() != bracketpair[s[i]]):
                    return False
            else:
                stack.append(s[i])
        
        if stack:
            return False
        return True
        
       



