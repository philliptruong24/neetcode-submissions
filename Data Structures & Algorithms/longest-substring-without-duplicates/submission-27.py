class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l = 0
        longest = 0
        for r in range(len(s)):
            if s[r] in count:
                l = max(count[s[r]] + 1, l)
            count[s[r]] = r
            longest = max(longest, r - l + 1)
        
        return longest


