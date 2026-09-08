class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def dfs(i):
            if i == len(s):
                res.append(curr.copy())
                return

            word = ""
            for j in range(i, len(s)):
                word += s[j]
                if self.isPalindrome(word):
                    curr.append(word)
                    dfs(j + 1)

                    curr.pop()
                
        dfs(0)

        return res
        
            

        
    def isPalindrome(self, s: str) -> bool: 
        if len(s) == 0:
            return False
        elif len(s) == 1:
            return True
        i, j = 0, len(s) - 1
        
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
    
        return True