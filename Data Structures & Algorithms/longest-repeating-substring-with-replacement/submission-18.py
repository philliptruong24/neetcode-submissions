class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = [0] * 26
        maxfreq = 0
        l = 0
        longest = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            maxfreq = max(maxfreq, count[ord(s[r]) - ord('A')])

            if r - l + 1 - maxfreq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        
        return longest

