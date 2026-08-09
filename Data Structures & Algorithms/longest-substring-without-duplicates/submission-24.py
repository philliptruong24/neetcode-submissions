class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        longest = 0
        i = 0

        for r in range(len(s)):
            if s[r] in mp:
                i = max(i, mp[s[r]] + 1)
            
            mp[s[r]] = r
            longest = max(longest, r - i + 1)
        
        return longest


