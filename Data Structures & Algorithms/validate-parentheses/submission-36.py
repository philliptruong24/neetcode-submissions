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
                if stack and stack[-1] == bracketpair[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        return True if not stack else False
        
       



