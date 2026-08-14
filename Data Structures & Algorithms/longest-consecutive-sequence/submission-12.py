class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for num in hashset:
            length = 1
            if num - 1 not in hashset:
                while num + length in hashset:
                    length += 1
            
            longest = max(length, longest)
        
        return longest

