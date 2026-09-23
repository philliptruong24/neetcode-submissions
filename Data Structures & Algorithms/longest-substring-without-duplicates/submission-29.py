class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        longest = 0
        curr = 0
        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    curr -= 1
                    seen.remove(s[l])
                    l += 1
                
            seen.add(s[r])
            curr += 1
            longest = max(longest, curr)
        return longest


