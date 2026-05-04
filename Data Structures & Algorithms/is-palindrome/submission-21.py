class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = s.lower()
        i, j = 0, len(n) - 1

        while i < j:
            while i < j and not n[i].isalnum():
                i += 1
            while i < j and not n[j].isalnum():
                j -= 1
            if (n[i] != n[j]):
                return False
            i += 1
            j -= 1
        return True
