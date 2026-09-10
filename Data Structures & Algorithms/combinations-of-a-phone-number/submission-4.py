class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        charMap = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        def dfs(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            
            digit = digits[i]
            for char in charMap[digit]:
                curr += char
                dfs(i + 1, curr)
                curr = curr[:-1]
            
        if not digits:
            return []
        dfs(0, "")
        return res