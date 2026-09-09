class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def dfs(i):
            if i == len(s):
                res.append(curr.copy())
                return

            for j in range(i, len(s)):
                word = s[i:j + 1]
                if self.isPalindrome(word):
                    curr.append(word)
                    dfs(j + 1)

                    curr.pop()
                
        dfs(0)
        return res
        
    def isPalindrome(self, s: str) -> bool: 
        if len(s) == 1:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
    
        return True