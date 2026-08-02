class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        sequence = []
        for num in seen:
            if (num - 1) not in seen:
                sequence.append([num])
        
        for s in sequence:
            while (s[-1] + 1) in seen:
                s.append(s[-1] + 1)
        
        length = 0
        for i in range(len(sequence)):
            if len(sequence[i]) > length:
                length = len(sequence[i])
        
        return length
