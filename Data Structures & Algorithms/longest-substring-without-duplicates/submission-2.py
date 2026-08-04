class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        l = 0
        r = 1
        seen = set()
        longest = 1
        seen.add(s[l])

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1

            longest = max(longest, r - l)


        return longest
    